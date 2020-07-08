from django.contrib import admin

from .models import *

admin.site.register(Company)

admin.site.register(Service)

admin.site.register(Employee)

admin.site.register(Client)

admin.site.register(Request)

admin.site.register(Payment)

admin.site.register(Product)
