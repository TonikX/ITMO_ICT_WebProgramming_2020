from django.urls import path

from quests.api import views

app_name = 'quests'
urlpatterns = [
    path('', views.QuestListView.as_view(), name='quests-list'),
    path('<int:pk>/', views.QuestDetailView.as_view(), name='quest-detail'),
    path('tasks', views.TaskCreateView.as_view(), name='tasks-list'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('answers', views.AnswerCreateView.as_view(), name='answer-list'),
    path('answers/<int:pk>', views.AnswerDetailView.as_view(), name='answer-detail')
]
