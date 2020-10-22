from django.urls import path

from .views import *

urlpatterns = [
    path('', authors_list, name='authors_board_url'),
    path('project_first_app/<str:slug>/', author_detail, name='author_detail_url')
]