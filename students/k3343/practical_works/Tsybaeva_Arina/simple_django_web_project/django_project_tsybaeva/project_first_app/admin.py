from django.contrib import admin

#Register your models here.
from project_first_app.models import Owner
from project_first_app.models import Auto
from project_first_app.models import Ocupation

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Ocupation)
