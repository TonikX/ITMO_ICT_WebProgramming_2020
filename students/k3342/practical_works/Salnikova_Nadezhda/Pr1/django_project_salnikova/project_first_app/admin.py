from django.contrib import admin
from project_first_app.models import Owner, Car, DriverLicense, Ownership


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    list_display_links = ('first_name', 'last_name', 'date_of_birth')


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'brand', 'model', 'color')
    list_display_links = ('car_number', 'brand', 'model', 'color')


class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'date_of_issue', 'category', 'owner')
    list_display_links = ('license_number', 'date_of_issue', 'category', 'owner')


class OwnershipAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car', 'date_of_start', 'date_of_end')
    list_display_links = ('owner', 'car', 'date_of_start', 'date_of_end')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(DriverLicense, DriverLicenseAdmin)
admin.site.register(Ownership, OwnershipAdmin)
