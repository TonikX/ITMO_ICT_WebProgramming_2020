from django.urls import path
from . import views

urlpatterns = [
    path('hotels', views.hotels, name='hotels'),
    path('comments', views.comments, name='comments'),
    path('new_comment', views.NewCommentView.as_view, name='new_comment'),
    path('register', views.RegisterView.as_view(), name='register')
]