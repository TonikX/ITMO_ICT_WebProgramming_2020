from django.contrib import admin

# Register your models here.
from .models import Owner, License, Car, Ownership

admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Car)
admin.site.register(Ownership)