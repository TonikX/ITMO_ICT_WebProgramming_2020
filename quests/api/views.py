from rest_framework import generics

from quests.api.serializers import QuestListSerializer, QuestDetailSerializer, TaskCreateSerializer, TaskDetailSerializer, \
    AnswerCreateSerializer, AnswerDetailSerializer
from quests.models import Quest, Task, Answer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerDetailSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class QuestListView(generics.ListCreateAPIView):
    queryset = Quest.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestListSerializer
        return QuestDetailSerializer


class QuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestDetailSerializer
