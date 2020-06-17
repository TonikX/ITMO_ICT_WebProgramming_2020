from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ConferenceView

urlpatterns = [
    path('', views.index,),
    path('index/', views.index),
    path('conferences/', ConferenceView.as_view()),
    path('conferences/<int:conf_id>/', views.about_conf),
]