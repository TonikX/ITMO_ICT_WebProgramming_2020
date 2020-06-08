from django.contrib import admin

# Register your models here.
from .models import Company, Flight, Comment

admin.site.register(Company)
admin.site.register(Flight)
admin.site.register(Comment)

