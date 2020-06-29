from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


app_name = "hotel"

urlpatterns = [
	path('floor/new', CreateFloorView.as_view()),
	path('floor/<int:pk>', RetrieveFloorView.as_view()),
	path('floor/all', ListFloorView.as_view()),
	path('room/new', CreateRoomView.as_view()),
	path('room/<int:pk>', RetrieveRoomView.as_view()),
	path('room/all', ListRoomView.as_view()),
	path('client/new', CreateClientView.as_view()),
	path('client/<int:pk>', RetrieveClientView.as_view()),
	path('client/all', ListClientView.as_view()),
	path('client/room/new', CreateClientRoomView.as_view()),
	path('client/room/<int:pk>', RetrieveClientRoomView.as_view()),
	path('client/room/all', ListClientRoomView.as_view()),
	path('cleaning/new', CreateCleaningView.as_view()),
	path('cleaning/<int:pk>', RetrieveCleaningView.as_view()),
	path('cleaning/all', ListCleaningView.as_view()),
	path('challenger/new', CreateChallengerView.as_view()),
	path('request/new', CreateRequestView.as_view()),
	path('request/update/<int:pk>', UpdateRequestView.as_view()),
	path('request/all', RetrieveReuqestView.as_view()),
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token')
]
