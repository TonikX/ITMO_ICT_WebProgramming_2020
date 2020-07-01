from urllib import request
from django.urls import path
from django.contrib.auth import views as view
from . import views
from .views import RegisterUserView, ClientRegistration, AddCommentClass

urlpatterns = [
    path('', views.main, name='main'),
    path('all_flights', views.show_flights, name='all_flights'),
    path('accounts/profile/', ClientRegistration.as_view, name='profile_page'),
    path('add_comment', AddCommentClass.as_view, name='add_comment'),
    path('all_comments', views.show_comments, name='all_comments'),
    path('login/', view.LoginView.as_view(), name='login'),
    path('logout/', view.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
]
