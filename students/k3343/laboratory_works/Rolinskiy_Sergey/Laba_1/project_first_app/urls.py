from django.urls import path
from django.conf.urls import url
from project_first_app.views import *

urlpatterns = [
    path('',main,name='main'),
    path('createowner/',createowner,name='createowner'),
    path('login/',log_in,name='login'),
    path(r'<int:ho_id>',review,name='detail')
]
#path(r'getowners/<int:ow_id>',detail,name='detail'),