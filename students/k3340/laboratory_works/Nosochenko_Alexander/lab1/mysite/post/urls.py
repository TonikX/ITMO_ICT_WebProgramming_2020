from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_list, name="list_info"),
    path('single/<int:pk>', views.single_info, name="single_info"),
    path('/accounts/login', views.single_info,  name="login")
]