from django.urls import path
from . import views
from .views import detail
from .views import CarList
from .views import add_owners
from .views import add_cars

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('owner_list/', views.owner_list),
    path('cars/', CarList.as_view()),
    path('add_owners/', views.add_owners),
    path('add_cars/', add_cars.as_view()),
]
