from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owner/<int:id>', views.owner, name='owner'),
]