from django.contrib import admin

from .models import Owner, Car, Driver_license, Ownership

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Driver_license)
admin.site.register(Ownership)