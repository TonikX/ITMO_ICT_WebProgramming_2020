from django.urls import path

from quests.api import views

app_name = 'quests'
urlpatterns = [
    path('', views.QuestListView.as_view(), name='quests-list'),
    path('<int:pk>/', views.QuestDetailView.as_view(), name='quest-detail'),
    path('<int:pk>/statistic', views.QuestStatisticDetailView.as_view(), name="quest-statistic"),
    path('<int:pk>/join', views.QuestJoinView.as_view(), name="quest-join"),
]
