from django.contrib import admin

# Register your models here.

from .models import Tour,Comment

admin.site.register(Tour)
admin.site.register(Comment)