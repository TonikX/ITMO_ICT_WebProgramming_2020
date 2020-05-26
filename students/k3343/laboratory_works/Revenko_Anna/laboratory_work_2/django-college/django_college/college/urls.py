from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


app_name = "college"

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token'),
	path('applications/', GetAllApplicationView.as_view()),
	path('specializations/', GetAllSpecializationView.as_view()),

]
