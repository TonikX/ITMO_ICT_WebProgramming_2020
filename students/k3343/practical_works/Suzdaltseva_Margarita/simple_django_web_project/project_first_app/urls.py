from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('owner/<int:carowner_id>', views.owner_info),
    path('time/', views.time_info),
    path('ownerlist/', views.ownerlist),
    path('carlist/', views.CarList.as_view()),
    path('owner_form/', views.create_owner),
    path('car_form/', views.CarCreate.as_view(success_url='car_form/')),
]
