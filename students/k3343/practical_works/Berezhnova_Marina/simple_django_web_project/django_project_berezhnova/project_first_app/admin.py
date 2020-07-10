from django.contrib import admin
from .models import User
from .models import Auto
from .models import Ownership
from .models import DriverLicense

# Register your models here.

admin.site.register(User)
admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
