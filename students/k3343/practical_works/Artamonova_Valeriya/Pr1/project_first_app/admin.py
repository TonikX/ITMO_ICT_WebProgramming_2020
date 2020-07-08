from django.contrib import admin
from .models import Auto_owner, Automobile, Driver_license, Owning


admin.site.register(Auto_owner)
admin.site.register(Automobile)
admin.site.register(Driver_license)
admin.site.register(Owning)

# Register your models here.
