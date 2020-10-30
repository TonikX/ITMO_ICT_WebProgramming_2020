from urllib import request

from django.urls import path
from django.contrib.auth import views as view
from . import views

urlpatterns = [
    path('', views.show_flights, name='all_flights'),
    path('aviacompany', views.show_aviacompanies, name='all_aviacompanies'),
    path('single/<int:pk>', views.show_flight_single, name="single_flight"),
]