from django.contrib import admin
from django.urls import path, include
from .views import detail

urlpatterns = [
    path('auto/<int:poll_id>/', detail),
]