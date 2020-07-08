from django.contrib import admin

from .models import Car_owner, Car, Ownership, Drivers_lic

admin.site.register(Car_owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(Drivers_lic)
