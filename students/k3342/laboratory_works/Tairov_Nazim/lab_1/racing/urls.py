from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.main, name='main'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('comments/', views.comments, name='comments'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_request, name='logout'),
]
