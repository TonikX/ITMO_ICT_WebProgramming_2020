from django.contrib import admin

# Register your models here.
from .models import  Car, Owner, Ownership, License

admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(License)
