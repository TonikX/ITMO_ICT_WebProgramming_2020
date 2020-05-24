from django.contrib import admin
from .models import AutoOwner
from .models import Auto
from .models import DriverLicense
from .models import Owner


admin.site.register(AutoOwner)
admin.site.register(Auto)
admin.site.register(DriverLicense)
admin.site.register(Owner)

