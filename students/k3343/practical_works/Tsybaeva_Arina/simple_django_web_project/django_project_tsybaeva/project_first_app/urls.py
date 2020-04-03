from django.urls import path
from . import views
from .views import AutoList

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('', views.AutoList.as_view())
]