from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('auto/<int:auto_id>', views.show_auto),
        path('owner/<int:owner_id>', views.show_owner)
]

