from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.owner_info),
    path('time/', views.time_info),
    path('owner_list/', views.owner_list),
    path('car_list/', views.CarList.as_view()),
    path('add_owner/', views.add_owner),
    path('add_car/', views.AddCar.as_view(success_url='add_car/')),
    path('info/', views.InfoList.as_view()),
]