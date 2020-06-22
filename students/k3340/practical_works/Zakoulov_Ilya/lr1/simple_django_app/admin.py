from django.contrib import admin
from .models import Driver, Car, DriverLicense, CarDriverOwn


admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(CarDriverOwn)
