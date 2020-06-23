from django.urls import path
from django.contrib.auth import views as view
from . import views

urlpatterns = [
    path('', views.show_hotels, name='all_hotels'),
    path('single_hotel/<int:pk>', views.show_hotel_single, name="single_hotel"),
]