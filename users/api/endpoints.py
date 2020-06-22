from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api import views

app_name = 'users'
urlpatterns = [
    path('questMaker', views.QuestMakerListView.as_view(), name='quest-maker-list'),
    path('team', views.TeamListView.as_view(), name='team-register-list'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
