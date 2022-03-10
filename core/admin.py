from django.contrib import admin
from core.models import *


class DatasetAdmin(admin.ModelAdmin):
    list_display = ['datasetName']


class Object3dAdmin(admin.ModelAdmin):
    list_display = ['objectId', 'label', 'container']


class ModalityAdmin(admin.ModelAdmin):
    list_display = ['modalityType', 'path', 'host']


admin.site.register(Dataset, DatasetAdmin)
admin.site.register(Object3d, Object3dAdmin)
admin.site.register(Modality, ModalityAdmin)
