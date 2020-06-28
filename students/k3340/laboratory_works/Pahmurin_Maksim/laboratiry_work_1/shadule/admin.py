from django.contrib import admin
from .models import *


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'homework', 'text', 'type', 'importance')


admin.site.register(Homework)
admin.site.register(Teacher)
admin.site.register(Comments, CommentAdmin)