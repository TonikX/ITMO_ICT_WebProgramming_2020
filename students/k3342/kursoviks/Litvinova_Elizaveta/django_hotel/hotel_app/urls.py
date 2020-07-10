from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


app_name = "hotel_app"

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/token/', obtain_auth_token, name='token'),

	path('floor/add/', NewFloorView.as_view()),
	path('floor/<int:pk>/', GetFloorView.as_view()),
	path('floors/', AllFloorView.as_view()),

	path('room/add/', NewRoomView.as_view()),
	path('room/<int:pk>/', GetRoomView.as_view()),
	path('rooms/', AllRoomView.as_view()),

	path('client/add/', NewClientView.as_view()),
	path('client/<int:pk>/', GetClientView.as_view()),
	path('clients/', AllClientView.as_view()),

	path('client/room/add/', NewClientRoomView.as_view()),
	path('client/room/<int:pk>/', GetClientRoomView.as_view()),
	path('client/rooms/', AllClientRoomView.as_view()),

	path('cleaning/add/', NewCleaningView.as_view()),
	path('cleaning/<int:pk>/', GetCleaningView.as_view()),
	path('cleanings/', AllCleaningView.as_view()),

	path('employee/add/', NewEmployeeView.as_view()),
	path('employee/<int:pk>/', GetEmployeeView.as_view()),
	path('employees/', AllEmployeeView.as_view()),
]
