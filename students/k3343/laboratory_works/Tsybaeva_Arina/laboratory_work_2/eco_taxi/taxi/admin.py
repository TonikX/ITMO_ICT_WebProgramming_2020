from django.contrib import admin
from .models import Category, Storage, Client, Driver, Order
# Register your models here.
admin.site.site_title = "Eco Taxi"
admin.site.site_header = "Eco Taxi"
admin.site.register(Category)
admin.site.register(Storage)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(Order)