from django.urls import path
from . import views
from .views import AutoCreate
urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('', AutoCreate.as_view())
]