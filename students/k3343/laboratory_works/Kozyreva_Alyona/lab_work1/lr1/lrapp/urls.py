from django.urls import path
from django.contrib.auth import views as view
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('start/', views.start),
    path('index/', views.index, name='index'),
    path('reg_user/', views.RegUserView.as_view(), name='reg_user'),
    path('reg_name/', views.reg_name, name='reg_name'),
    path('board/', views.board, name='board'),
    path('comments/', views.comments_list, name='comments'),
    path('comment/', views.comment, name='comment'),
]
