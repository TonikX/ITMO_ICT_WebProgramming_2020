from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = 'django_app'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('workers', WorkerListView.as_view()),
    path('cages', CageListView.as_view()),
    path('chickens', ChickenListView.as_view()),
    path('chickens/add', AddChickenView.as_view()),
    path('reports', ReportListView.as_view()),
    path('reports/add', AddReportView.as_view()),
]
