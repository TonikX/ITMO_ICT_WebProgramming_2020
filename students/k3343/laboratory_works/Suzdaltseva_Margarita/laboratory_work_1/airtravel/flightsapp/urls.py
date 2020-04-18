from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.flights_list, name="flights_list"),
    path('single/<int:pk>', views.flight_single, name="flight_single"),
    path('filter/<int:pk>', views.flights_type, name="flights_type"),
]