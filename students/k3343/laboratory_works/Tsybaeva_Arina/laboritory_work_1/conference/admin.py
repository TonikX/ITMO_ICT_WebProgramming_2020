from django.contrib import admin
from conference.models import Scientist, Conference, Section, Comment

# Register your models here.
admin.site.register(Scientist)
admin.site.register(Conference)
admin.site.register(Section)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'conference', 'created')
    search_fields = ('name', 'email', 'body', 'comment_type')


admin.site.register(Comment, CommentAdmin)