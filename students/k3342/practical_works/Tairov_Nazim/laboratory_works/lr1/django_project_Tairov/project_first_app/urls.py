from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owner/<int:id>', views.owner, name='owner'),
    path('list_view/', views.list_view, name='list_view'),
    path('list_car/', views.CarsView.as_view(), name='list_car'),
    path('create_owner/', views.create_owner, name='create_owner'),
    path('create_car/', views.CreateCar.as_view(), name='create_car'),

]