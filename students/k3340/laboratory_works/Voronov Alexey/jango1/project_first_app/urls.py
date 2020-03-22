from django.contrib import admin
from django.urls import path, include
from project_first_app import views

urlpatterns = [
    path('person/<int:poll_id>/', views.detail),
]