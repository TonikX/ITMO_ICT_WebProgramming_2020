from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from django.conf import settings

urlpatterns = [
    path('', table, name='table_url'),
    path('exp/<int:dr_id>', show_exp, name='driver_exp_url'),
    path('comments/<int:dr_id>', show_comments, name='all_comm_url'),
    path('add_comm/<int:dr_id>', add_comment, name='add_comm_url'),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
