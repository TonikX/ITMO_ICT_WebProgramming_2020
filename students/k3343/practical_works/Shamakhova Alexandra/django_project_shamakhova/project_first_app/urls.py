from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:car_owner_id>/', views.car_owner_info),
    path('owner_list/', views.car_owner_list),
    path('car_list/', views.CarList.as_view()),
    path('owner_form/', views.car_owner_form),
    path('car_form/', views.CarForm.as_view(success_url='http://127.0.0.1:8000/car_form/')),
]
