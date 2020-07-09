"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('patients/', Patients.as_view()),
    path('patient/<int:pk>/', PatientDetail.as_view()),
    path('app/<int:pk>/', AppointmentDetail.as_view()),
    path('patient/<int:pk>/edit/', PatientUpdate.as_view()),
    path('patient/<int:pk>/delete/', PatientDelete.as_view()),
    path('med_card/', MedCard.as_view()),
    path('doctors/', Doctors.as_view()),
    path('schedule/', ScheduleView.as_view()),
    path('add_doc/', CreateDoctor.as_view()),
    path('app_times/', AppTimesList.as_view()),
    path('apps/', Apps.as_view()),
    path('appointments/', Appointments.as_view()),
    path('app_detail/', AppDetail.as_view()),
    path('add_app/', CreateApp.as_view()),
    path('app/<int:pk>/edit/', AppUpdate.as_view()),
    path('doc_free_time/', DocFreeTime.as_view()),
    path('services/', Services.as_view()),
    path('query_1/', QuerySet1.as_view()),
    path('query_2/', QuerySet2.as_view()),
    path('query_3/', QuerySet3.as_view()),
    path('query_4/', QuerySet4.as_view()),
    path('report/', Report.as_view()),
    # path('filter_app/', AppFilterView.as_view()),
]
