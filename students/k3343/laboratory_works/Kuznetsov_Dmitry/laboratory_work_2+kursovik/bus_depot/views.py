from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Sum

from .service import ScheduleFilter, JournalFilter, DriverFilter
from .models import BusType, Bus, Driver, Route, Schedule, Journal
from .serializers import BusTypeSerializer, BusSerializer, DriverSerializer, RouteSerializer, ScheduleSerializer, \
    JournalSerializer, BusCreateSerializer, ScheduleCreateSerializer, JournalCreateSerializer


class BusTypeViewSet(viewsets.ModelViewSet):
    """Отображение для модели Тип автобуса"""
    queryset = BusType.objects.all()
    serializer_class = BusTypeSerializer


class BusViewSet(viewsets.ModelViewSet):
    """Отображение для модели Автобус"""
    queryset = Bus.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return BusCreateSerializer
        elif self.action == 'update':
            return BusCreateSerializer
        else:
            return BusSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """Отображение для модели Водитель"""
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = DriverFilter


class RouteViewSet(viewsets.ModelViewSet):
    """Отображение для модели Маршрут"""
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """Отображение для модели Расписание"""
    queryset = Schedule.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = ScheduleFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return ScheduleCreateSerializer
        elif self.action == 'update':
            return ScheduleCreateSerializer
        else:
            return ScheduleSerializer


class JournalViewSet(viewsets.ModelViewSet):
    """Отображение для модели Журнал"""
    queryset = Journal.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = JournalFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return JournalCreateSerializer
        elif self.action == 'update':
            return JournalCreateSerializer
        else:
            return JournalSerializer

    """Запросы к курсовой работе"""


class Query3(APIView):
    """Какова общая протяженность маршрутов, обслуживаемых автопарком?"""
    def get(self, request):
        results_km = Route.objects.aggregate(total_length=Sum('length_in_km'))
        results_min = Route.objects.aggregate(total_length=Sum('length_in_min'))
        return Response({'result': [results_km, results_min]})


class Query5(APIView):
    """Сколько водителей каждого класса работает в автопарке?"""
    def get(self, request):
        results = Driver.objects.values('driver_class').order_by('driver_class').annotate(Count('fio'))
        return Response({'result': results})
