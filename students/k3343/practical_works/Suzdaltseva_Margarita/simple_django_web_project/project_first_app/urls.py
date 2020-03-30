from django.contrib import admin
from django.urls import path, include
from . import views
# from .views import ExampleList

urlpatterns = [
    path('owner/<int:carowner_id>', views.owner_info),
    path('time/', views.time_info),
    path('examplef/', views.list_view),
    path('examplec/', views.ExampleList.as_view()),
    path('ownerlist/', views.ownerlist),
    path('carlist/', views.CarList.as_view()),
]
