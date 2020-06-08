from django.contrib import admin
from .models import Autoholder, Automobile, Holding, Drivers_license, AdditionalData

admin.site.register(Autoholder)
admin.site.register(Automobile)
admin.site.register(Holding)
admin.site.register(Drivers_license)
admin.site.register(AdditionalData)

