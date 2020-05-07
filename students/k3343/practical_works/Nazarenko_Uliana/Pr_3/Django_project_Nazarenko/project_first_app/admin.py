from django.contrib import admin

from .models import CarOwner, Car, DriversLicense, Ownership, Info


admin.site.register(Car)

admin.site.register(DriversLicense)

admin.site.register(Ownership)

admin.site.register(Info)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username','name', 'surname', 'birth_date', 'passport', 'address', 'nationality')

admin.site.register(CarOwner, OwnerAdmin)