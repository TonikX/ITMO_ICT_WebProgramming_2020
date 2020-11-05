from django.urls import path, include
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_info),
]