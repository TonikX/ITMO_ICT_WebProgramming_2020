from rest_framework import generics

from users.api.serializerts import QuestMakerSerializer, TeamSerializer
from users.models import User


class QuestMakerListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_quest_maker=True)
    serializer_class = QuestMakerSerializer


class TeamListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(is_quest_maker=False)
    serializer_class = TeamSerializer
