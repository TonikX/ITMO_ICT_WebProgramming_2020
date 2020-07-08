from django.urls import path
from . import views

urlpatterns = [
    path('tour/<int:tour_id>', views.tour, name="tour_one"),
    path('tour/list_view', views.TourList.as_view())
]