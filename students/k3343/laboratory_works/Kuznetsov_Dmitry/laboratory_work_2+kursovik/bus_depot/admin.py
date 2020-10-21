from django.contrib import admin
from .models import BusType, Bus, Driver, Route, Schedule, Journal

admin.site.register(BusType)
admin.site.register(Bus)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Journal)
# Register your models here.
