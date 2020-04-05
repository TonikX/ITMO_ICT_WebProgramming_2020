from django.urls import path
from django.conf.urls import url
from project_first_app.views import *

urlpatterns = [
    path(r'getowners/<int:ow_id>',detail,name='detail')
]
