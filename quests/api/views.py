from rest_framework import generics
from rest_framework.exceptions import ValidationError

from quests.api.serializers import QuestListSerializer, QuestDetailSerializer, TaskCreateSerializer, \
    TaskDetailSerializer, \
    AnswerCreateSerializer, AnswerDetailSerializer, TipCreateSerializer, TipDetailSerializer, \
    PenaltyTimeCreateSerializer, PenaltyTimeDetailSerializer
from quests.models import Quest, Task, Answer, Tip, PenaltyTime


class PenaltyTimeCreateView(generics.CreateAPIView):
    queryset = PenaltyTime.objects.all()
    serializer_class = PenaltyTimeCreateSerializer


class PenaltyTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PenaltyTime.objects.all()
    serializer_class = PenaltyTimeDetailSerializer

    def perform_destroy(self, instance):
        quest = instance.quest
        max_count_tips = 0
        for task in quest.tasks.all():
            max_count_tips = max(max_count_tips, task.tips.count())
        count_penalty_times = quest.penalty_times.count()
        if count_penalty_times <= max_count_tips:
            raise ValidationError("You have to remove extra tips first")
        super().perform_destroy(instance)


class TipCreateView(generics.CreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipCreateSerializer

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        quest = task.quest
        count_tips = task.tips.count()
        count_penalty_times = quest.penalty_times.count()
        if count_tips >= count_penalty_times:
            raise ValidationError(f'You have to declare {count_tips + 1} penalty times')
        super().perform_create(serializer)


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
