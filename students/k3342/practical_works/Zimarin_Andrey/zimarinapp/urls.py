from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars),
    path('owner/<int:owner_id>', views.owner)
]