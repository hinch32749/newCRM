from django.contrib import admin
from . import models

admin.site.register(models.CarInGarage)
admin.site.register(models.City)
admin.site.register(models.Promotion)
admin.site.register(models.Service)

