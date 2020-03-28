from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('auto', views.AutoView.as_view()),
        path('owner/<int:owner_id>', views.show_owner)
]
