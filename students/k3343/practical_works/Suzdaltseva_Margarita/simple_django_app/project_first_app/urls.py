from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('owner/<int:carowner_id>', views.owner_info)
]