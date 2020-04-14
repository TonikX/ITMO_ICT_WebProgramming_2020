from django.contrib import admin

# Register your models here.
from .models import Owner

admin.site.register(Owner)

from .models import DrivingLicense, Car, Ownership

admin.site.register(DrivingLicense)
admin.site.register(Car)
admin.site.register(Ownership)

