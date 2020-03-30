from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:owner_id>', views.owner_info),
        path('owners/', views.owners_info),
        path('cars/', views.CarsView.as_view())
]
