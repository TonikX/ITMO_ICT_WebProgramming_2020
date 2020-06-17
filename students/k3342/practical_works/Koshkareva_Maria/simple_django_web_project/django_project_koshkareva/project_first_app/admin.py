from .models import Owner, Car, Driver_license, Ownership
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets
        (
            'Their new info',  # group heading
            {
                'fields': (
                    'passport','address','nationality'
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Driver_license)
admin.site.register(Ownership)
