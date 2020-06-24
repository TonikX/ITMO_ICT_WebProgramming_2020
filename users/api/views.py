from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.api.serializerts import QuestMakerSerializer, TeamSerializer
from users.models import User
from users.permissions import IsSuperuser


class QuestMakerListView(generics.ListCreateAPIView):
    permission_classes = (IsSuperuser, )
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = QuestMakerSerializer


class TeamListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = User.objects.filter(is_staff=False)
    serializer_class = TeamSerializer


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, )
    queryset = User.objects.filter(is_staff=False)
    serializer_class = TeamSerializer
