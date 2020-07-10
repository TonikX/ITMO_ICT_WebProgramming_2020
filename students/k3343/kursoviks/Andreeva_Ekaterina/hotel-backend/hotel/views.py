from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .service import CleaningFilter
from collections import Counter
from django.db.models import Count, Avg

from .models import Floor, RoomType, Room, Resident, Servant, Cleaning
from .serializers import FloorSerializer, RoomTypeSerializer, RoomSerializer, ResidentSerializer,\
    ResidentCreateSerializer, ServantSerializer, CleaningSerializer, CleaningCreateSerializer


class FloorViewSet(viewsets.ModelViewSet):
    """Отображение для модели Этаж"""
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    """Отображение для модели Тип Комнаты"""
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """Отображение для модели Комната"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    """Отображение для модели Проживающий"""
    queryset = Resident.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ResidentCreateSerializer
        elif self.action != 'create':
            return ResidentSerializer


class ServantViewSet(viewsets.ModelViewSet):
    """Отображение для модели Служащий"""
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer


class CleaningViewSet(viewsets.ModelViewSet):
    """Отображение для модели Уборка"""
    queryset = Cleaning.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = CleaningFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CleaningCreateSerializer
        elif self.action != 'create':
            return CleaningSerializer


"""Запросы к курсовой работе"""


class Query1(APIView):
    """о клиентах, проживавших в заданном номере"""

    def get(self, request):
        room = request.GET.get('room_number')
        #room = '1'
        resident_list = Resident.objects.filter(room=room)
        serializer = ResidentSerializer(resident_list, many=True)
        return Response({'result': serializer.data})


class Query3(APIView):
    """о том, кто из служащих убирал номер указанного клиента в заданный день недели"""

    def get(self, request):
        room = request.GET.get('resident')
        day = request.GET.get('day')
        #room = '1'
        #day = 'Понедельник'
        floor1 = Room.objects.filter(room_number=room)[0].floor
        servant1 = Cleaning.objects.filter(floor=floor1, day=day)[0].servant
        result = str(servant1)
        return Response({'result': result})


class Query2(APIView):
    """о количестве клиентов, прибывших из заданного города"""

    def get(self, request):
        results = Resident.objects.values('from_town').order_by('from_town').annotate(Count('fio'))
        return Response({'result': results})


class Query4(APIView):
    """сколько в гостинице свободных номеров"""

    def get(self, request):
        floor1 = Floor.objects.filter(floor_number=1)[0].number_of_rooms
        floor2 = Floor.objects.filter(floor_number=2)[0].number_of_rooms
        rooms = Room.objects.all().aggregate(Count('id'))['id__count']
        results = floor1+floor2-rooms
        return Response({'result': results})


# Create your views here.
