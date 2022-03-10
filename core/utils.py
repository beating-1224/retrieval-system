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
    results = None
    for dataset in datasets:
        dataset = Dataset.objects.filter(datasetName=dataset)
        dataset = dataset.first()
        result = Object3d.objects.filter(label=label, container=dataset)
        results = result if results is None else results | result
    all_ms = None
    for obj in results:
        for modality in modalities:
            ms = obj.modality.filter(modalityType=MODALITY_CODE[modality])
            all_ms = ms if all_ms is None else ms | all_ms
    ret = []
    for ms in all_ms:
        ret.append(str(ms))
    return choices(ret, k=30)
