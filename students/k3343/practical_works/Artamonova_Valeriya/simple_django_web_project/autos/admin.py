from django.contrib import admin
from .models import User, Automobile, DriverLicense, Owning

admin.site.register(User)
admin.site.register(Automobile)
admin.site.register(DriverLicense)
admin.site.register(Owning)
# Register your models here.
