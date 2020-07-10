from django.contrib import admin
from .models import *

class MalfunctionAd(admin.ModelAdmin):
    list_display = ('bus','date_start','piece','piece_now','date_close')

class ReportAd(admin.ModelAdmin):
    list_display = ('schedule_line','reason')

class DriverAd(admin.ModelAdmin):
    list_display = ('passport','d_of_b','name','surname','job_class','date_begin',
                  'work_exp','salary','bus','route')


class BusAd(admin.ModelAdmin):
    list_display = ('reg_plate','type','capacity')


class RouteAd(admin.ModelAdmin):
    list_display = ('num','loc_start','loc_end',
                  'time_start','time_end','interval_min',
                  'circle_time_min')

class ScheduleAd(admin.ModelAdmin):
    list_display = ('driver','bus','route','work_day',
                    'work_start','work_end')

admin.site.register(Driver,DriverAd)
admin.site.register(Malfunction, MalfunctionAd)
admin.site.register(Bus, BusAd)
admin.site.register(Route, RouteAd)
admin.site.register(Schedule, ScheduleAd)
admin.site.register(Report, ReportAd)