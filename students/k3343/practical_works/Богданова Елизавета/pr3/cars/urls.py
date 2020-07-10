from urllib import request

from django.urls import path
from . import views
from .views import Show_car, CarsCreate

urlpatterns = [
    path('all_owners', views.show_all_owners),
    path('all_cars', Show_car.as_view),
    path('create_automobiles',CarsCreate.as_view),
]