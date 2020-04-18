from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('time/', views.geeks_view),
    path('all_owners/', views.owners_list),
    path('all_cars/', views.CarList.as_view(template_name="cars.html")),
    path('add_owners/', views.create_view),
    path('add_cars/', views.CarCreate.as_view(template_name="create_car.html"))
]

