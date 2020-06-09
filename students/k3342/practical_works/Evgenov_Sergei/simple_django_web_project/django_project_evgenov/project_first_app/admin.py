from django.contrib import admin

# Register your models here.

from .models import Car
from .models import DrivingLicense
from .models import Ownership
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(Car)
admin.site.register(DrivingLicense)
admin.site.register(Ownership)
admin.site.register(User)
