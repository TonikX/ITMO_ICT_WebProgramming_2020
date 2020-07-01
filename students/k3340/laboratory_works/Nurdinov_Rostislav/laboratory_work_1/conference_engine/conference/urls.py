from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', conference, name='conference_url'),
    path('conf/<int:cid>/', detail, name='conf_detail_url'),
    path('about/', about, name='about_url'),
    path('archive/', archive, name='archive_url'),
    path('future/', future_conf, name='future_conf_url')
]