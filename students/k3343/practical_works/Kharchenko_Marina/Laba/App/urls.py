from django.urls import path
from . import views
from .views import AutoCreate, AutoList

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('', views.list_view),
    path('autos/', AutoList.as_view()),
    path('create_auto/', AutoCreate.as_view()),
    path('create_owner/', views.create_view())
]