from django.urls import path
from auto_racing_scoreboard import views
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('', views.main, name='main'),
	path('scoreboard/', views.scoreboard, name='scoreboard'),
	path('comments/', views.comments, name='comments'),
	path('register/', views.reg, name='register'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', views.LogoutFormView.as_view(), name='logout'),
]
