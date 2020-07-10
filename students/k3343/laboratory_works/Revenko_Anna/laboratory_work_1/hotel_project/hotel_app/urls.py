from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('login/', set_login),
	path('register/', register),
	path('hotels/list', HotelListView.as_view()),
	path('hotels/<int:hotel_id>', get_hotel),
]
