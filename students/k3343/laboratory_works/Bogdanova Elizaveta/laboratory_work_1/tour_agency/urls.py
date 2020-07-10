from urllib import request

from django.urls import path
from django.contrib.auth import views as view
from . import views
from .views import TouristRegistration, New_Comment, RegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('tours', views.show_tours, name='tours'),
    path('profile', TouristRegistration.as_view, name='profile'),
    path('new_comment', New_Comment.as_view, name='new_comment'),
    path('comments', views.show_comments, name='comments'),
    path('login/', view.LoginView.as_view(), name='login'),
    path('logout/', view.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
]