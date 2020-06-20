from django.contrib import admin
from .models import Teacher, Homework, Student, Comment

admin.site.register(Teacher)
admin.site.register(Student)

class HomeworksAdmin(admin.ModelAdmin):
    """ Новости"""
    list_display = ("subject", "teacher", "task", "deadline")

admin.site.register(Homework, HomeworksAdmin)

class CommentAdmin(admin.ModelAdmin):
    """ Комментарии"""
    list_display = ('user', 'task', 'date', 'type')

admin.site.register(Comment, CommentAdmin)