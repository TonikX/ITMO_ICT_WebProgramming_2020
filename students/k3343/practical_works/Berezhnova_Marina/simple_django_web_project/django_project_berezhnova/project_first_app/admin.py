from django.contrib import admin
from .models import Driver
from .models import Auto
from .models import Ownership
from .models import DriverLicense

# Register your models here.

admin.site.register(Driver)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
