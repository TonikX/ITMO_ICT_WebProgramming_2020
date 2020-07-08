from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(Conference)
admin.site.register(Section)
admin.site.register(Speaker)
admin.site.register(Lecture)
admin.site.register(Speech)
admin.site.register(Comment)

# Register your models here.
