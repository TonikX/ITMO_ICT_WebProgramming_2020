from django.urls import path

from users.api import views

app_name = 'users'
urlpatterns = [
    path('questMakers', views.QuestMakerListView.as_view(), name='quest-makers-list'),
    path('teams', views.TeamListView.as_view(), name='teams-list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail')
]
