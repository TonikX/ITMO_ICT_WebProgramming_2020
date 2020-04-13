from django.contrib import admin

from .models import Conference
admin.site.register(Conference)

from .models import Conference_themes
admin.site.register(Conference_themes)

from .models import Comment
admin.site.register(Comment)

from .models import Theme
admin.site.register(Theme)




