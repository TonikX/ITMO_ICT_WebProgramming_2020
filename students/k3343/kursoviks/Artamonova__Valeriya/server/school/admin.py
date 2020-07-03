from django.contrib import admin
from .models import UserProfile,Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade

admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Timetable)
admin.site.register(Klass)
admin.site.register(Pupil)
admin.site.register(Cabinet)
admin.site.register(Subject)
admin.site.register(Grade)
