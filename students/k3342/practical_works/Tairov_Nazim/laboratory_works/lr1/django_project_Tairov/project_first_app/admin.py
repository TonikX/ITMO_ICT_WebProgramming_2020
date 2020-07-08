from django.contrib import admin
from .models import (CarOwner, TemporaryOwner,
                     DriverLicense, Car)

my_models = [CarOwner, TemporaryOwner, DriverLicense, Car]

admin.site.register(my_models)
