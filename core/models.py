from django.db import models


class Dataset(models.Model):
    datasetName = models.CharField(max_length=100, verbose_name="dataset name")

    def to_dict(self):
        return {
            'dataset name': self.datasetName,
        }

    def __str__(self):
        return self.datasetName

    class Meta:
        verbose_name = 'Dataset Information'
        verbose_name_plural = verbose_name


class Object3d(models.Model):
    objectId = models.CharField(max_length=100, verbose_name="object id")
    label = models.CharField(max_length=100, verbose_name="object label")
    container = models.ForeignKey('Dataset', on_delete=models.CASCADE, related_name='containing', verbose_name="container")

    def to_dict(self):
        return {
            'object id': self.objectId,
        }

    def __str__(self):
        return self.objectId

    class Meta:
        verbose_name = 'Object Name'
        verbose_name_plural = verbose_name


class Modality(models.Model):
    modalityType = models.IntegerField(choices=((0, 'PointCloud'), (1, 'Voxel'), (2, 'MultiView')), verbose_name='modalityType')
    path = models.CharField(max_length=1000)
    host = models.ForeignKey('Object3d', on_delete=models.CASCADE, related_name='modality', verbose_name="host object")

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = 'Modality'
        verbose_name_plural = verbose_name
