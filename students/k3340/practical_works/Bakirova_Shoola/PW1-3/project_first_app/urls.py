from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>/', carowner),
    path('cars/', CarView.as_view()),
    path('owners/', owner_list),
    path('owner/new', new_owner),
    path('car/new', NewCar.as_view(success_url='/car/'))
]