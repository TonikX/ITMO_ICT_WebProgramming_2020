from django.contrib import admin
from django.urls import path, include
from project_first_app import views, forms

urlpatterns = [
    path('person/<int:poll_id>/', views.detail),
    path('persons', views.persons),
    path('vehicles', views.Vehicles.as_view()),
    path('add_vehicle', forms.AddVehicle.as_view()),
    path('add_person', views.addPerson),
]