from django.urls import path


from . import views


urlpatterns = [


    path('owner/<int:owner_id>/', views.detail),
    path('owners/', views.owners_detail),
    path('cars/', views.CarsView.as_view()),
    path('cars/add/', views.add_car),
    path('owners/add/', views.add_owner),
]