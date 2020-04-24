from django.contrib import admin
from hw.models import Comment, Homework

admin.site.register(Homework)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentator', 'comment_importance', 'comment_type', 'homework', 'created', 'moderation')

admin.site.register(Comment, CommentAdmin)

