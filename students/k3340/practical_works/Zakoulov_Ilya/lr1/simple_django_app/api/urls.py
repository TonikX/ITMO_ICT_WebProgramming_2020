from django.urls import path

from simple_django_app.api import views

app_name = 'simple_django_app'

urlpatterns = [
    path('cars/<int:car_id>', views.get),
]
