from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:owner_id>', views.get_owner_info),
        path('auto/<int:auto_id>', views.AutoInfoView.as_view())
]
