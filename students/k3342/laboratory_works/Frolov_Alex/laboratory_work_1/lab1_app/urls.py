from django.urls import path
from django.contrib.auth import views as view
from . import views
from .views import Add_Comment

urlpatterns = [
    path('', views.index, name='index'),
    path('all_conferences', views.show_conferences, name='all_conferences'),
    path('add_comment', Add_Comment.as_view, name='add_comment'),
    path('all_comments', views.show_comments, name='all_comments'),
]