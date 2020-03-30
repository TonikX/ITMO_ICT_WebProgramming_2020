from django.contrib import admin
from urllib import request
from django.urls import path
from .views import Show_car
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('all_owners', views.show_all_owners),
    path('all_cars', Show_car.as_view)
]