from django.contrib import admin
from .models import User, Car, Driver_license, Owning

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Driver_license)
admin.site.register(Owning)