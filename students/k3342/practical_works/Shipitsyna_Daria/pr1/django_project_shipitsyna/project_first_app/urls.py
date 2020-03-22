from django.urls import path
from .views import detail

urlpatterns = [
    path('owner/<int:owner_id>', detail),
]