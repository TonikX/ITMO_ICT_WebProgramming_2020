from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Climber)
admin.site.register(Group)
admin.site.register(Mountain)
admin.site.register(Climbing)
admin.site.register(Club)
admin.site.register(ClubOwner)

