from django.contrib import admin

from .models import Location, DanceStyle, Choreographer, Workshop, Comments, Master

admin.site.register(Location)
admin.site.register(DanceStyle)
admin.site.register(Choreographer)
admin.site.register(Workshop)
admin.site.register(Comments)
admin.site.register(Master)