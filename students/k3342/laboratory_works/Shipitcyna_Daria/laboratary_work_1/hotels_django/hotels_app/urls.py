from django.urls import path
from .views import hotels_list
from .views import hotel_single

urlpatterns = [
    path('', hotels_list),
    path('hotel_single/<int:pk>', hotel_single, name='hotel_single'),
]
