from django.contrib import admin

# Register your models here.

from .models import Owner, Car, Ownership, License

admin.site.register(Owner)

admin.site.register(Car)

admin.site.register(Ownership)

admin.site.register(License)


