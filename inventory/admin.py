from django.contrib import admin
from . import models



admin.site.register(models.Laptop)
admin.site.register(models.Desktop)
admin.site.register(models.Mobile)