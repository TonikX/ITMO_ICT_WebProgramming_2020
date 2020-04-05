from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.owner_inf),
    path('owner/', views.owner_inf),
    path('owners/', views.owners_inf),
    path('cars/', views.CarsView.as_view()),
    path('ownerform/', views.create_new_owner),
    path('carform/', views.CarCreate.as_view(success_url='carform/')),
]