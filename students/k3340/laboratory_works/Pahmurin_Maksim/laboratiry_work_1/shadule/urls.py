from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_table, name="homework_table"),
    path('single/<int:pk>/', views.homework_single, name="homework_single"),
]