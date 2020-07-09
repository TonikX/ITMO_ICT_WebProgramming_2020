from django.urls import path
from .views import detail
from .views import owner_list
from .views import CarList
from .views import create_owner
from .views import CarCreate

urlpatterns = [
    path('owner/<int:owner_id>', detail),
    path('owner_list', owner_list),
    path('car_list', CarList.as_view()),
    path('create_owner', create_owner),
    path('create_car', CarCreate.as_view())
]