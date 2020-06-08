from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('hotels/all', HotelAllView.as_view()),
	path('hotels/<int:hotel_id>', show_hotel),
	path('login/', user_login),
	path('register/', user_register)
]
