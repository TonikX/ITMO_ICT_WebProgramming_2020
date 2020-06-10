from django.urls import path

from users.api import views

app_name = 'users'
urlpatterns = [
    path('questMaker', views.QuestMakerListView.as_view(), name='quest-maker-list'),
    path('team', views.TeamListView.as_view(), name='team-register-list'),
]
