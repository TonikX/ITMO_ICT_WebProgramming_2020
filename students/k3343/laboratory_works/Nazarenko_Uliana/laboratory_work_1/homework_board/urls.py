from urllib import request

from django.urls import path
from django.contrib.auth import views as view
from . import views
from .views import User_registration, Comment_creation, RegisterUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('hw_list', views.hw_view, name='hwlist'),
    path('profile', User_registration.as_view, name='profile'),
    path('comment_creation', Comment_creation.as_view, name='commentcreation'),
    path('comments_list', views.comments_view, name='commentslist'),
    path('login/', view.LoginView.as_view(), name='login'),
    path('logout/', view.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterUserView.as_view(), name='register'),
]
