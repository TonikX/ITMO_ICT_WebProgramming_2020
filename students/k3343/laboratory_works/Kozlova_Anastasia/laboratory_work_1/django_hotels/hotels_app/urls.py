from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('hotels/', HotelView.as_view()),
	path('hotels/<int:hotel_id>/', hotel_info),
	path('accounts/login/', user_login),
	path('accounts/register/', register)
]
