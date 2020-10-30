from django.contrib import admin
from .models import Car, Team, RacerProfile, Race, Comment


admin.site.register(Car)
admin.site.register(Team)
admin.site.register(RacerProfile)
admin.site.register(Race)
admin.site.register(Comment)
