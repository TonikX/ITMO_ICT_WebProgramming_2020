from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from .models import *
from .serializers import *


class ClimberView(generics.ListAPIView):
    queryset = Climber.objects.all()
    serializer_class = ClimberSerializer


class ClimberAdd(generics.CreateAPIView):
    queryset = Climber.objects.all()
    serializer_class = AddClimberSerializer


class ClimberEdit(generics.UpdateAPIView):
    queryset = Climber.objects.all()
    serializer_class = AddClimberSerializer


class ClimberGet(generics.RetrieveAPIView):
    queryset = Climber.objects.all()
    serializer_class = ClimberSerializer


class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupAdd(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupEdit(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MountainView(generics.ListAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer


class MountainAdd(generics.CreateAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer


class MountainEdit(generics.RetrieveUpdateAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer


class MountainGet(generics.RetrieveAPIView):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer


class ClimbingView(generics.ListAPIView):
    serializer_class = ClimbingSerializer

    def get_queryset(self):
        queryset = Climbing.objects.all()

        params = self.request.query_params

        date1 = params.get('date_start', None)
        date2 = params.get('date_end', None)
        is_planned = params.get('is_planned', None)
        is_in_progress = params.get('is_in_progress', None)
        is_finished = params.get('is_finished', None)
        is_group = params.get('is_group', None)
        is_solo = params.get('is_solo', None)


        if date2:
            queryset = queryset.filter(climbing_date_end__lte=date2)

        if date1:
            queryset = queryset.filter(climbing_date_start__gte=date1)

        if is_planned and is_in_progress and is_finished:
            queryset = queryset.filter(Q(status="1") | Q(status='2') | Q(status='3'))
        elif is_planned and is_in_progress:
            queryset = queryset.filter(Q(status="1") | Q(status='2'))
        elif is_planned:
            queryset = queryset.filter(status="1")
        elif is_in_progress and is_finished:
            queryset = queryset.filter(Q(status='2') | Q(status='3'))
        elif is_in_progress:
            queryset = queryset.filter(status='2')
        elif is_finished:
            queryset = queryset.filter(status='3')

        if is_group and is_solo:
            queryset = queryset.filter(Q(group__isnull=False) | Q(climber__isnull=False))
        elif is_group:
            queryset = queryset.filter(group__isnull=False)
        elif is_solo:
            queryset = queryset.filter(climber__isnull=False)

        return queryset


class ClimbingAdd(generics.CreateAPIView):
    queryset = Climbing.objects.all()
    serializer_class = ClimbingSerializer


class ClimbingEdit(generics.RetrieveUpdateAPIView):
    queryset = Climbing.objects.all()
    serializer_class = ClimbingSerializer


class ClubAdd(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubEdit(generics.RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubOwnerAdd(generics.CreateAPIView):
    queryset = ClubOwner.objects.all()
    serializer_class = ClubOwnerSerializer


class ClubOwnerEdit(generics.RetrieveUpdateAPIView):
    queryset = ClubOwner.objects.all()
    serializer_class = ClubOwnerSerializer
    # objects.select_related()


class ClubOwnerView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubOwnerSerializer
# 1. Показать список альпинистов, осуществлявших восхождение в указанный
# интервал дат;
# 2. Показать список восхождений (групп), которые осуществлялись в
# указанный пользователем период времени
# 3. Предоставить информацию о том, сколько альпинистов побывали на каждой
# горе.
# 4. Предоставить данные о вершинах, если на них не было восхождений
# 5. Показать информацию о количестве восхождений каждого альпиниста на
# каждую гору.
