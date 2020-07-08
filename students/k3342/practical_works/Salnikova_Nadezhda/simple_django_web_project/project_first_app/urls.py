from django.urls import path
from . import views
from .views import CarList, CarCreate


urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail),
    path('owner_list', views.owner_list),
    path('owner_form', views.create_owner_view),
    path('car_list', CarList.as_view()),
    path('car_form', CarCreate.as_view())
]
