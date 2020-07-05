from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_profile, Teacher, Hometask, Comment


admin.site.register(Teacher)
admin.site.register(Hometask)
admin.site.register(Comment)

class UserInline(admin.StackedInline):
    model = User_profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


