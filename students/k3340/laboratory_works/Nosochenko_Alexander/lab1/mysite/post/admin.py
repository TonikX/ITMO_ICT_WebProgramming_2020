from django.contrib import admin
from post.models import *

admin.site.register(Info)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('client', 'text', 'info')


admin.site.register(Comment, CommentAdmin)
