from django.contrib import admin
from urllib import request
from django.urls import path
from .views import Show_car, create_view_owners, CarsCreate
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('all_owners', views.show_all_owners),
    path('all_cars', Show_car.as_view),
    path('create_owners', create_view_owners),
    path('create_cars', CarsCreate.as_view),
]