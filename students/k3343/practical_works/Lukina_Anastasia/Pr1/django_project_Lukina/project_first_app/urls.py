from django.urls import path
from . import views
from .views import detail

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail)
]