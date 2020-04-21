from django.urls import path
from . import views

urlpatterns = [
    path('afisha/', views.wsh_list),
    path('single/<int:pk>', views.workshop_single, name='Workshop_single'),
]
