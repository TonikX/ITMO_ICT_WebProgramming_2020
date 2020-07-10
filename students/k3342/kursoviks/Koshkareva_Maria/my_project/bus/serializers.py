from rest_framework import serializers

from .models import *


class BusSerializers(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    class Meta:
        model = Bus
        #fields = ('id','reg_plate','type','capacity')
        fields = '__all__'


class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        '''fields = ('id','num','loc_start','loc_end',
                  'time_start','time_end','interval_min',
                  'circle_time_min')'''
        fields = '__all__'


class DriverSerializers(serializers.ModelSerializer):
    bus = BusSerializers()
    route = RouteSerializers()

    class Meta:
        model = Driver
        '''fields = ('id','passport','d_of_b','job_class','date_begin',
                  'work_exp','salary','bus','route')'''
        fields = "__all__"


class DriverPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Driver
        '''fields = ('id','passport','d_of_b','job_class','date_begin',
                  'work_exp','salary','bus','route')'''
        fields = ('passport','d_of_b','job_class','date_begin',
                  'bus','route','name','surname')


class DriverDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id')


class MalfunctionSerializers(serializers.ModelSerializer):
    bus = BusSerializers()
    #piece_now = serializers.MultipleChoiceField(choices=[1,2,3,4,5,6,7,8])
    #piece = serializers.CharField(source='get_piece_display')
    #piece_now = serializers.CharField(source='get_piece_display')

    class Meta:
        model = Malfunction
        fields = "__all__"

class MalfunctionPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Malfunction
        fields = ('bus','date_start','piece')


class ScheduleSerializers(serializers.ModelSerializer):
    driver = DriverSerializers()
    bus = BusSerializers()
    route = RouteSerializers()

    class Meta:
        model = Schedule
        fields = ('id','driver','bus','route', 'work_day',
                  'work_start','work_end')


class SchedulePostSerializers(serializers.ModelSerializer):
    #driver = DriverSerializers()
    #bus = BusSerializers()
    #route = RouteSerializers()

    class Meta:
        model = Schedule
        fields = ('driver','bus','route', 'work_day',
                  'work_start','work_end')

class ScheduleDelSerializers(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id')


class SchedulePutSerializers(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'


class ReportSerializers(serializers.ModelSerializer):
    reason = serializers.CharField(source='get_reason_display')
    schedule_line = ScheduleSerializers()

    class Meta:
        model = Report
        fields = '__all__'


class ReportPutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

