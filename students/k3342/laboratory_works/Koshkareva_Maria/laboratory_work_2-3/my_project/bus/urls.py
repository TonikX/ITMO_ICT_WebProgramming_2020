from django.urls import path
from .views import *

urlpatterns = [
    path('driver/', Drivers.as_view()),
    path('malfunction/', Malfunctions.as_view()),
    path('malfunction/<int:pk>/', Malfunctions_detail.as_view()),
    path('all_drivers/', AllDrivers.as_view()),
    path('route/', Routes.as_view()),
    path('one_route/', Routes_detail.as_view()),
    path('schedule/', Schedules.as_view()),
    path('schedule/<int:pk>/', Schedules_detail.as_view()),
    path('driver/<int:pk>/', Drivers_detail.as_view()),
    path('schedule_r/', Schedules_R.as_view()),
    path('bus/', Buses.as_view()),
    path('buses_status/', BusesStatus.as_view()),
    path('schedule_reports/', SchedReport.as_view()),
    path('schedule_report/<int:pk>/', SchedReport_detail.as_view()),
# report
    path('report_buses/', Report_buses.as_view()),
# queries
    path('dr_on_r/', DriverOnRoute.as_view()),
    path('bus_on_r/', BusOnRoute.as_view()),
    path('routes_time/', RouteTime.as_view()),
    path('bad_report/', BusReport.as_view()),
    path('dr_class/', DriverClass.as_view()),
]