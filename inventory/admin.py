from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


@admin.register(models.Laptop, models.Desktop, models.Mobile)
class InventoryAdmin(ImportExportModelAdmin):
    pass
