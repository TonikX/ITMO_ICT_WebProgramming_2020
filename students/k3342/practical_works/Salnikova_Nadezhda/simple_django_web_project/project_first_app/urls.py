from django.urls import path
from . import views
from .views import CarList


urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail),
    path('owner_list', views.owner_list),
    path('car_list', CarList.as_view())
]
