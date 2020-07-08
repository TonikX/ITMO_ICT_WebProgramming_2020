from django.contrib import admin

# Register your models here.

from .models import Owner, License, Car, Ownership

admin.site.register(License)
admin.site.register(Car)
admin.site.register(Ownership)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'passport', 'address', 'nationality')


admin.site.register(Owner, OwnerAdmin)

