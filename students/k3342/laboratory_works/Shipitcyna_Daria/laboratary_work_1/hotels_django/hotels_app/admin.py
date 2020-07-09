from django.contrib import admin
from .models import Facilities
from .models import Room_types
from .models import Hotel
from .models import Comment

admin.site.register(Facilities)
admin.site.register(Room_types)
admin.site.register(Hotel)
admin.site.register(Comment)
