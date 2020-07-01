from django.contrib import admin
from django.contrib.auth.models import User
from .models import Flight, Comment, AviaCompany


admin.site.register(Flight)
admin.site.register(Comment)
admin.site.register(AviaCompany)
# Register your models here.
