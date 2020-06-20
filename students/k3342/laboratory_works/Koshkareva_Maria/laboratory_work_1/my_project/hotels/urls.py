from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.HotelsList.as_view(), name='hotel-main'),
    path('info/<int:hotel_id>/', views.hotel_info, name='hotel-info'),
]
