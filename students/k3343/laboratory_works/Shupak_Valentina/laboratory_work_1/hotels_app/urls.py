from django.urls import path
from django.contrib import admin
from . import views
from .views import HotelView

urlpatterns = [
    path('', views.main, name='main'),
    path('main/',views.main),
    path('hotels/', HotelView.as_view()),
    path('hotels/<int:hotel_id>/', views.about_hotel),
]