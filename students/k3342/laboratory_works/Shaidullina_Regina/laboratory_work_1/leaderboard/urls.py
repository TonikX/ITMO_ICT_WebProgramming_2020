from django.contrib import admin
from django.urls import path
from leaderboard import views
from django.contrib.auth.views import LoginView  #, LogoutView

urlpatterns = [
	path('', views.main, name='main'),
	path('leaderboard/', views.leaderboard_view, name='leaderboard'),
	path('comments/', views.comments, name='comments'),
	path('register/', views.reg, name='register'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', views.LogoutFormView.as_view(), name='logout'),
]
