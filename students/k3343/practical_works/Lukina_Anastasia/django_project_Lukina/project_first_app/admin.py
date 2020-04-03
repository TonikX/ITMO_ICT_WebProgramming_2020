from django.contrib import admin

# Register your models here.
from .models import CarOwner
admin.site.register(CarOwner)

from .models import DrivingLicense
admin.site.register(DrivingLicense)

from .models import Owning
admin.site.register(Owning)

from .models import Car
admin.site.register(Car)

from .models import GeeksModel
admin.site.register(GeeksModel)


