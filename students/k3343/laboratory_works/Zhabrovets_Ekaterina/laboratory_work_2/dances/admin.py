from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(Hall)
admin.site.register(DanceStyle)
admin.site.register(Choreographer)
admin.site.register(Participant)
admin.site.register(Workshop)