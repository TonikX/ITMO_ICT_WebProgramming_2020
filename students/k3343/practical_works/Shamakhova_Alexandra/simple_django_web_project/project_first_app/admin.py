from django.contrib import admin

# Register your models here.

from .models import CarOwner

admin.site.register(CarOwner)

from .models import Car

admin.site.register(Car)

from .models import Ownership

admin.site.register(Ownership)

from .models import DriversLicense

admin.site.register(DriversLicense)
