from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(Hall)
admin.site.register(DanceStyle)
admin.site.register(Workshop)
admin.site.register(User)
admin.site.register(QueryForParticipance)
admin.site.register(QueryForTuition)
admin.site.register(Feedback)