from django.urls import path
from project_first_app.views import detail

urlpatterns = [
    path('owner/<int:Car_owner_id>', detail),
]
