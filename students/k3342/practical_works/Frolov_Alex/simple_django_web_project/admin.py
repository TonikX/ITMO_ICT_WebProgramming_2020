from django.contrib import admin
from .models import User, Avto, License, Ownership

admin.site.register(Avto)
admin.site.register(License)
admin.site.register(Ownership)
admin.site.register(User)

