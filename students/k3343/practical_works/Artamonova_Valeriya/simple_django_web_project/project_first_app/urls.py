from urllib import request

from django.urls import path
from . import views
from .views import Show_auto, create_view_owners, AutomobilesCreate

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('all_owners', views.show_all_owners),
    path('all_cars', Show_auto.as_view),
    path('create_owners', create_view_owners),
    path('create_automobiles', AutomobilesCreate.as_view),
]