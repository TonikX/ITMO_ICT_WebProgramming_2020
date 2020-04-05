from django.urls import path
from django.conf.urls import url
from project_first_app.views import *

urlpatterns = [
    path(r'getowners/<int:ow_id>',detail,name='detail'),
    path(r'allowners',show_owners,name='showowners'),
    path(r'allcars', Show_cars.as_view(template_name="cars_list.html")),
    path(r'createowners',createowner,name='createowner'),
    path('createcars/', Car_create.as_view()),
]
