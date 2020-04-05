from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_info),
    path('owners_list/', views.owners_list),
    path('cars_list/', views.CarsList.as_view()),
    path('create_owner/', views.create_owner),
    path('car_form/', views.CreateCar.as_view()),
]
