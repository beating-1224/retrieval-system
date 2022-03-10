import os

from django.http import HttpResponse

from core.models import Dataset

from core.const import DATASETS_URL


def update_datasets(request):
    # dataset = Dataset()
    # dataset.datasetName = 'testDataset'
    # dataset.save()
    # dataset = Dataset.objects.filter(datasetName='')
    # dataset.delete()
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
                        print(os.path.join(DATASETS_URL, dataset, label, obj, modality))
                        files = os.listdir(os.path.join(DATASETS_URL, dataset, label, obj, modality))
                        if files:
                            for file in files:
                                file = os.path.join(DATASETS_URL, dataset, label, obj, modality, file)
                                assert file.split('.')[-1] == 'png'

        # for dataset in datasets:
        #     d = Dataset()
        #     d.datasetName = dataset
        #     d.save()
        #     labels = os.listdir(os.path.join(DATASETS_URL, dataset))
        #     for label in labels:
        #         objs = os.listdir(os.path.join(DATASETS_URL, dataset, label))
        #         for obj in objs:
        #             modalities = os.listdir(os.path.join(DATASETS_URL, dataset, label, obj))
        #             for modality in modalities:
        #                 print(os.path.join(DATASETS_URL, dataset, label, obj, modality))
        #                 files = os.listdir(os.path.join(DATASETS_URL, dataset, label, obj, modality))
        #                 if files:
        #                     for file in files:
        #                         file = os.path.join(DATASETS_URL, dataset, label, obj, modality, file)
        #                         assert file.split('.')[-1] == 'png'
    except Exception as e:
        print(e)
        return HttpResponse('fail')

    return HttpResponse('okk')


def get_datasets(request):
    return HttpResponse('okk')


def get_samples(request):
    return HttpResponse('okk')


def upload(request):
    return HttpResponse('okk')


def edit_pool_dataset(request):
    return HttpResponse('okk')


def edit_pool_modality(request):
    return HttpResponse('okk')


def search_sample(request):
    return HttpResponse('okk')


def search_file(request):
    return HttpResponse('okk')
