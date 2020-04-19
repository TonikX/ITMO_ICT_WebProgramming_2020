from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:carowner_id>', views.carowner)
]