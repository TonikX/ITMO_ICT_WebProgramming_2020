from django.urls import path
from . import views
from .views import LoginFormView, LogoutFormView
urlpatterns =[
    path('', views.show_conferences, name='all_conferences'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('all_comments', views.comments, name='all_comments'),
    path('all_sections/', views.detail, name='all_sections'),
    path('register/', views.register, name='register')
]