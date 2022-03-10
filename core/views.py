import os
from itertools import chain

from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from core.models import Dataset, Object3d, Modality

from core.const import DATASETS_URL
from random import choices, choice

from core.utils import retrieval


def update_datasets(request):
    try:
        datasets = os.listdir(DATASETS_URL)
        # validate first
        for dataset in datasets:
            labels = os.listdir(os.path.join(DATASETS_URL, dataset))
            for label in labels:
                objs = os.listdir(os.path.join(DATASETS_URL, dataset, label))
                for obj in objs:
                    modalities = os.listdir(os.path.join(DATASETS_URL, dataset, label, obj))
                    for modality in modalities:
                        file = os.path.join(DATASETS_URL, dataset, label, obj, modality)
                        assert modality.split('.')[0] == 'pt' or 'voc' or 'mv'
                        assert file.split('.')[-1] == 'png'

        # clear old
        Dataset.objects.all().delete()
        Object3d.objects.all().delete()
        Modality.objects.all().delete()

        # create new
        for dataset in datasets:
            d = Dataset(datasetName=dataset)
            d.save()
            labels = os.listdir(os.path.join(DATASETS_URL, dataset))
            for label in labels:
                objs = os.listdir(os.path.join(DATASETS_URL, dataset, label))
                for obj in objs:
                    o = Object3d(objectId=obj, label=label, container=d)
                    o.save()
                    modalities = os.listdir(os.path.join(DATASETS_URL, dataset, label, obj))
                    for modality in modalities:
                        file = os.path.join(DATASETS_URL, dataset, label, obj, modality)
                        m = Modality(path=file, host=o)
                        if modality.split('.')[0] == 'pt':
                            m.modalityType = 0
                        elif modality.split('.')[0] == 'vox':
                            m.modalityType = 1
                        elif modality.split('.')[0] == 'mv':
                            m.modalityType = 2
                        else:
                            raise Exception('unknown modality type')
                        m.save()

    except Exception as e:
        print(e)
        return JsonResponse({'error': 'format wrong'}, status=403)

    return JsonResponse({'message': 'ok'})


def get_datasets(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'require GET'}, status=400)
    all_datasets = Dataset.objects.all()
    ret = []
    for d in all_datasets:
        ret.append(str(d))
    return JsonResponse({'datasets': ret})


@csrf_exempt
def get_samples(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'require GET'}, status=400)
    # data = QueryDict(request.body)
    # datasets = data.get('datasets')
    datasets = request.GET.get('datasets', '')
    datasets = datasets.split(',')
    all_obj = None
    for dataset in datasets:
        dataset = Dataset.objects.filter(datasetName=dataset)
        dataset = dataset.first()
        objs = Object3d.objects.filter(container=dataset)
        all_obj = objs if all_obj is None else all_obj | objs
    sample_obj = choices(all_obj, k=40)
    ret = []
    for obj in sample_obj:
        mods = Modality.objects.filter(host=obj)
        mod = choice(mods)
        ret.append(str(mod))

    return JsonResponse({'samples': ret})


def upload(request):
    return HttpResponse('okk')


def search_sample(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'require GET'}, status=400)
    query = request.GET.get('query', '')
    datasets = request.GET.get('datasets', '')
    datasets = datasets.split(',')
    modalities = request.GET.get('modalities', '')
    modalities = modalities.split(',')
    ret = retrieval(datasets, modalities, query, k=50)
    return JsonResponse({'samples': ret})


def search_file(request):
    return HttpResponse('okk')
