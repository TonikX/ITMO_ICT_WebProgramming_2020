from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
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

    def get_serializer_class(self):
        if self.action == 'create':
            return CleaningCreateSerializer
        elif self.action != 'create':
            return CleaningSerializer
# Create your views here.
