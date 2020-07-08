from django.urls import path

# importing views from views..py
from .views import geeks_view

urlpatterns = [
    path('time/', geeks_view),
]