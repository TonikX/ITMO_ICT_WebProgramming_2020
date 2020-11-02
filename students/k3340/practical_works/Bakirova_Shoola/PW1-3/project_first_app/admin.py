from django.contrib import admin
from .models import Car, DrivingLicense, Ownership
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(Car)
admin.site.register(DrivingLicense)
admin.site.register(Ownership)
admin.site.register(User)
