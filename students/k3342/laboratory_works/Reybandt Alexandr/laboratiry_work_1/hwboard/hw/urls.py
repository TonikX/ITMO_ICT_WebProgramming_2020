from django.urls import path

from .views import *

urlpatterns = [
    path('', hw_list, name='hw_list_url'),
    path('comments_list/', comments_list, name='comments_list_url'),
    path('<int:pk>/', hw_detail, name='hw_detail_url')
]