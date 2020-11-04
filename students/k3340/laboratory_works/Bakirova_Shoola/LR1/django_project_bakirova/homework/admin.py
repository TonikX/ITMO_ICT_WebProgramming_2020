from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Homeworks, ImportanceComments, TypeComments, Comments


class HomeworkAdmin(SummernoteModelAdmin):
    """ Доска домашних заданий
    """
    list_display = ("title", "user", "created", "duration")
    list_editable = ("user",)
    search_fields = ["title", "user__username"]
    list_filter = ("user", "created")
    summer_note_fields = 'text'


class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'homework', 'importance', 'created', 'type', 'moderation')


admin.site.register(Homeworks, HomeworkAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(ImportanceComments)
admin.site.register(TypeComments)
