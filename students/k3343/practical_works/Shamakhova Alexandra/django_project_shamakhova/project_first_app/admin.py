from django.contrib import admin
from .models import User as CarOwner, Car, Ownership, DriverLicense


admin.site.register(CarOwner)

admin.site.register(Car)

admin.site.register(Ownership)

admin.site.register(DriverLicense)



#class OwnerAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'date_of_birth', 'passport', 'address', 'ethnicity')


#admin.site.register(CarOwner, OwnerAdmin)