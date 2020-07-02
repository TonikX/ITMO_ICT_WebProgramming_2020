from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('tours/', TourView.as_view()),
	path('tours/<int:tour_id>/', about_tour),
	path('auth/', auth),
	path('register/', register)
]
