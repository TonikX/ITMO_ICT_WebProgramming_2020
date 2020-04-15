from django.contrib import admin

# Register your models here.
from .models import Owner, Auto, Ownership, Licence

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Licence)
admin.site.register(Ownership)
