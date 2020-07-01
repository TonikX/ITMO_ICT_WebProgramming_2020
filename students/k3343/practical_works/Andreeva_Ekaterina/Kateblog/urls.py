from django.contrib import admin
from urllib import request
from django.urls import path
from . import views
from .views import detail

urlpatterns = [
path('owner/<int:owner_id>', views.detail)
]
