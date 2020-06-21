from django.contrib import admin

# Register your models here.

from .models import Owner, Car, Ownership, License

admin.site.register(Car)

admin.site.register(Ownership)

admin.site.register(License)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birth_date', 'passport', 'nationality')


admin.site.register(Owner, OwnerAdmin)
