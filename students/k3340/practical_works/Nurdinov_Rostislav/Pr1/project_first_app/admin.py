from django.contrib import admin
from .models import Auto, Owner, Ownership, License

admin.site.register(Auto)
admin.site.register(Ownership)
admin.site.register(Owner)
admin.site.register(License)
