from django.contrib import admin
from .models import CarOwner, Car, Ownership, DriverLicense
from django.contrib.auth.admin import UserAdmin

# admin.site.register(CarOwner)

admin.site.register(Car)

admin.site.register(Ownership)

admin.site.register(DriverLicense)


#class OwnerAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'date_of_birth', 'passport', 'address', 'ethnicity')


#admin.site.register(CarOwner, OwnerAdmin)

class Admin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':
                    ('first_name', 'last_name', 'date_of_birth', 'passport', 'address', 'ethnicity')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':
                    ('first_name', 'last_name', 'date_of_birth', 'passport', 'address', 'ethnicity')}),
    )