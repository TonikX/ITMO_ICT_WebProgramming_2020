from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('flights/', views.FlightView.as_view()),
	path('flights/<int:flight_id>/', views.show_flight),
	path('accounts/login/', views.user_login),
	path('accounts/register/', views.register),
	path('logout/', views.logout)
]
