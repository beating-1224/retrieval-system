from random import choices

from django.db.models import Q

from core.models import Dataset, Object3d, Modality

MODALITY_CODE = {
    'pt': 0,
    'vx': 1,
    'vox': 1,
    'mv': 2
}


def retrieval(datasets, modalities, query, k=50):
    # fake search
    m = Modality.objects.filter(path=query)
    m = m.first()
    obj = m.host
    label = obj.label
    results = []
    for dataset in datasets:
        dataset = Dataset.objects.filter(datasetName=dataset)
        dataset = dataset.first()
        result = Object3d.objects.filter(label=label, container=dataset)
        for r in result:
            results.append(r)
    ret = []
    for obj in results:
        for modality in modalities:
            ms = obj.modality.filter(modalityType=MODALITY_CODE[modality])
            for m in ms:
                ret.append(str(m))
    if len(ret) > k:
        return choices(ret, k=k)
    else:
        return ret
