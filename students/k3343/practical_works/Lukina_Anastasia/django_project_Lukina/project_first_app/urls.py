from django.urls import path
from . import views
from .views import detail
from .views import list_view
from .views import all_owners_output
from .views import GeeksList
from .views import CarsList
from .views import create_view
from .views import add_car_owners
from .views import add_cars
from .views import GeeksCreate


urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('list_view/', views.list_view),
    path('all_owners_output/', views.all_owners_output),
    path('geekslist', GeeksList.as_view()),
    path('all_cars_output/', CarsList.as_view()),
    path('create_view/', views.create_view),
    path('add_car_owners/', views.add_car_owners),
    path('geekcreate/', GeeksCreate.as_view()),
    path('add_cars/', add_cars.as_view()),
]
