from django.urls import path
from . import views
from .views import owners
from .views import create_view
from .views import CarCreate

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('all_owners_output/', views.owners),
    path('all_cars_output/', CarsList.as_view()),
    path('create_view/', views.create_view),
    path('add_car_owners/', views.owners),
    path('add_cars/', CarCreate.as_view()),
]