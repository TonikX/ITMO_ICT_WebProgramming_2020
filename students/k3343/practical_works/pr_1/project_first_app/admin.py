from django.contrib import admin
from .models import Car_owner, Car, Driver_license, Owning

admin.site.register(Car_owner)
admin.site.register(Car)
admin.site.register(Driver_license)
admin.site.register(Owning)

