from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
from django.db.models import Count, Avg
from .models import Flight, AirCarrier, Crew, TransitLanding, Route, Plane, CrewCommander, SecondPilot, Steward, Navigator
from .serializers import FlightSerializer, AirCarrierSerializer, CrewSerializer, CrewCommanderSerializer, \
                        CrewFIOCommanderSerializer, TransitLandingSerializer, RouteSerializer, PlaneSerializer,\
                        SecondPilotSerializer, SecondPilotFIOSerializer, StewardSerializer, StewardFIOSerializer, \
                        NavigatorSerializer, NavigatorFIOSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """Отображение для модели Рейс"""
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class AirCarrierViewSet(viewsets.ModelViewSet):
    """Отображение для модели Авиаперевозчик"""
    queryset = AirCarrier.objects.all()
    serializer_class = AirCarrierSerializer


class CrewViewSet(viewsets.ModelViewSet):
    """Отображение для модели Экипаж"""
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """Отображение для модели Маршрут"""
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class TransitViewSet(viewsets.ModelViewSet):
    """Отображение для модели Транзитная посадка"""
    queryset = TransitLanding.objects.all()
    serializer_class = TransitLandingSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    """Отображение для модели Самолет"""
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class CrewCommanderViewSet(viewsets.ModelViewSet):
    """Отображение для модели Командир экипажа"""
    queryset = CrewCommander.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return CrewFIOCommanderSerializer
        elif self.action != 'update':
            return CrewCommanderSerializer


class SecondPilotViewSet(viewsets.ModelViewSet):
    """Отображение для модели Второй пилот"""
    queryset = SecondPilot.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return SecondPilotFIOSerializer
        elif self.action != 'update':
            return SecondPilotSerializer


class StewardViewSet(viewsets.ModelViewSet):
    """Отображение для модели Бортпроводник"""
    queryset = Steward.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return StewardFIOSerializer
        elif self.action != 'update':
            return StewardSerializer


class NavigatorViewSet(viewsets.ModelViewSet):
    """Отображение для модели Штурман"""
    queryset = Navigator.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return NavigatorFIOSerializer
        elif self.action != 'update':
            return NavigatorSerializer


"""Запросы к курсовой работе"""


class Query3(APIView):
    """Определить наличие свободных мест на заданный рейс."""

    def get(self, request):
        number = request.GET.get('number')
        plane = str(Flight.objects.filter(id=number)[0].plane)
        number_of_seats = Plane.objects.filter(id=plane)[0].number_of_seats
        number_of_tickets = Flight.objects.filter(id=2)[0].number_of_tickets
        results = number_of_seats-number_of_tickets
        return Response({'result': results})


class Query4(APIView):
    """Определить количество самолетов, находящихся в ремонте."""

    def get(self, request):
        results = Plane.objects.filter(on_repairing=True).count()
        return Response({'result': results})


class Query5(APIView):
    """Определить количество работников аэропорта"""

    def get(self, request):

        crew_commander = CrewCommander.objects.count()
        second_pilot = SecondPilot.objects.count()
        navigator = Navigator.objects.count()
        stewards = Steward.objects.count()
        all_employees = crew_commander+second_pilot+navigator+stewards
        return Response({'result': all_employees})


class AirCarrierReport(APIView):
    """отчет о бортах компании-владельца по маркам с характеристикой марки"""

    def get(self, request):

        aircarrier = request.GET.get('aircarrier')
        planes = Plane.objects.values("number", 'number_of_seats', 'on_repairing', 'speed', 'type').filter(air_carrier=aircarrier)
        all_planes = planes.count()
        planes_by_type = Plane.objects.values('type').filter(air_carrier=aircarrier).order_by('type').annotate(Count('type'))
        results = {
                'planes': planes,
                'all_planes': all_planes,
                'planes_by_type': planes_by_type,
            }
        return Response({'result': results})

# Create your views here.
