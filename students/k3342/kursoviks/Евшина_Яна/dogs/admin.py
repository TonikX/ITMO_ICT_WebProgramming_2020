from django.contrib import admin
from .models import User, Dog, Perform, Ring, \
    Show, Club, Grade, Registration

# Register your models here.

admin.site.register(User)
admin.site.register(Dog)
admin.site.register(Perform)
admin.site.register(Ring)
admin.site.register(Show)
admin.site.register(Club)
admin.site.register(Grade)
admin.site.register(Registration)
