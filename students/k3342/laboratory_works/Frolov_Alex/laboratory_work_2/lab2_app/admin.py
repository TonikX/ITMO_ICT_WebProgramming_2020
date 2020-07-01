from django.contrib import admin
from .models import UserProfile, Teacher, Timetable, Nclass, Children, Room, Subject, Grade

admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Timetable)
admin.site.register(Nclass)
admin.site.register(Children)
admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Grade)

# Register your models here.
