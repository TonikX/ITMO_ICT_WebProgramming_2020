from rest_framework import generics

from quests.api.serializers import QuestListSerializer, QuestDetailSerializer, TeamStatisticListSerializer, \
    QuestStatisticListSerializer, QuestStatisticSerializer
from quests.models import Quest
from quests.permissions import IsAdminOrReadOnly


class QuestListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Quest.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestListSerializer
        return QuestDetailSerializer


class QuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Quest.objects.all()
    serializer_class = QuestDetailSerializer


class QuestStatisticDetailView(generics.RetrieveAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestStatisticListSerializer


class QuestJoinView(generics.CreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestStatisticSerializer

    def perform_create(self, serializer):
        serializer.save(team=self.request.user, quest_id=self.kwargs['pk'])
