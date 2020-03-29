from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.Owner_info),
    path('owners_list/', views.Owners_list),
    path('cars_list/', views.Cars_list.as_view()),
]
