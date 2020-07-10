from django.contrib import admin
from .models import Floor, RoomType, Room, Resident, Servant, Cleaning

admin.site.register(Floor)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Servant)
admin.site.register(Cleaning)
# Register your models here.
