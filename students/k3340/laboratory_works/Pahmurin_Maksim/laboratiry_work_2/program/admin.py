from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'class_number')


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'group')


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):

    list_display = ('name', )

@admin.register(Shedule)
class SheduleAdmin(admin.ModelAdmin):

    list_display = ('time', 'teacher', 'subject', 'group')


admin.site.register(Rating)
admin.site.register(Group)
