from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:carowner_id>', views.carowner),
    path('owner/list/', views.list_view),
    path('car/list/', views.CarList.as_view()),
    # path('form/owner/', views.create_view),
    path('form/car/', views.CarCreate.as_view()),
    path('form/car/success/', views.success)
]