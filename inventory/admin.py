from django.contrib import admin
from . import models


@admin.register(models.Laptop, models.Desktop, models.Mobile)
class InventoryAdmin(admin.ModelAdmin):
    pass
