from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


app_name = "college_comission_app"

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
	path('applications/all', ApplicationListView.as_view()),
	path('applications/new', ApplicationNewView.as_view()),
	path('applications/<int:pk>', ApplicationView.as_view()),
	path('specializations/all', SpecListView.as_view()),
	path('specializations/<int:pk>', SpecView.as_view()),
	path('enrollee/all', EnrolleeListView.as_view()),
	path('enrollee/new', EnrolleeNewView.as_view()),
	path('enrollee/<int:pk>', EnrolleeView.as_view()),
]
