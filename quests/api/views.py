from rest_framework import generics

from quests.api.serializers import QuestListSerializer, QuestDetailSerializer, TaskCreateSerializer, \
    TaskDetailSerializer, \
    AnswerCreateSerializer, AnswerDetailSerializer, TipCreateSerializer, TipDetailSerializer, \
    PenaltyTimeCreateSerializer, PenaltyTimeDetailSerializer
from quests.models import Quest, Task, Answer, Tip, PenaltyTime


class PenaltyTimeCreateView(generics.CreateAPIView):
    queryset = PenaltyTime.objects.all()
    serializer_class = PenaltyTimeCreateSerializer


class PenaltyTimeDetailView(generics.CreateAPIView):
    queryset = PenaltyTime.objects.all()
    serializer_class = PenaltyTimeDetailSerializer


class TipCreateView(generics.CreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipCreateSerializer


class TipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipDetailSerializer


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
