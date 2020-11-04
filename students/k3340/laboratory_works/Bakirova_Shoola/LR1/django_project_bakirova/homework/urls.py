# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_list, name="homework_list"),
    path('single/<int:pk>', views.homework_single, name="homework_single"),
]