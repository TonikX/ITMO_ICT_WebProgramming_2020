from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('human/all', HumanListView.as_view()),
    path('human/new', CreateHumanView.as_view()),
    path('human/<int:pk>', GetHumanView.as_view()),

    path('dogs/all', DogsListView.as_view()),
    path('dogs/new/', CreateDogView.as_view()),
    path('dogs/<int:pk>', GetDogView.as_view()),

    path('experts/all', ExpertsListView.as_view()),
    path('experts/new/', CreateExpertView.as_view()),
    path('experts/<int:pk>', GetExpertView.as_view()),

    path('funders/all', FundersListView.as_view()),
    path('funders/new/', CreateFunderView.as_view()),
    path('funders/<int:pk>', GetFunderView.as_view()),

    path('rings/all', RingsListView.as_view()),
    path('rings/new/', CreateRingView.as_view()),
    path('rings/<int:pk>', GetRingView.as_view()),

    path('shows/all', ShowsListView.as_view()),
    path('shows/new/', CreateShowView.as_view()),
    path('shows/<int:pk>', GetShowView.as_view()),

    path('records/all', RecordsListView.as_view()),
    path('records/new/', CreateRecordView.as_view()),
    path('records/<int:pk>', GetRecordView.as_view()),

    path('acts/all', ActsListView.as_view()),
    path('acts/new/', CreateActView.as_view()),
    path('acts/<int:pk>', GetActView.as_view()),

    path('sponsors/all', SponsorsListView.as_view()),
    path('sponsors/new/', CreateSponsorView.as_view()),
    path('sponsors/<int:pk>', GetSponsorView.as_view()),

    path('judgings/all', JudgingsListView.as_view()),
    path('judgings/new/', CreateJudgingView.as_view()),
    path('judgings/<int:pk>', GetJudgingView.as_view()),

    path('ifclient', IfClientView.as_view()),

    # path('org', GetOrganizerView.as_view()),
]
