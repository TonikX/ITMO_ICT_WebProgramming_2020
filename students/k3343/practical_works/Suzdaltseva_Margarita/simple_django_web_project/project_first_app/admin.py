from django.contrib import admin

from .models import CarOwner, Car, DriversLicense, Ownership

#admin.site.register(CarOwner)

admin.site.register(Car)

admin.site.register(DriversLicense)

admin.site.register(Ownership)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'birth_date', 'passport', 'address', 'nationality')

admin.site.register(CarOwner, OwnerAdmin)