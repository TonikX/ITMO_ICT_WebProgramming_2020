from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
from django.db.models import Count, Avg
from .models import Faculty, Specialty, Enrollee, Application,EGE, EgeSubject, Attestat, AttestatSubject
from .serializers import FacultySerializer, SpecialtySerializer, EnrolleeSerializer, ApplicationSerializer, \
    ApplicationCreateSerializer, EgeSerializer, EgeCreateSerializer, AttestatSerializer, AttestatCreateSerializer, \
    EgeSubjectSerializer, AttestatSubjectSerializer, EnrolleeDetailSerializer


class AttestatViewSet(viewsets.ModelViewSet):
    """CRUD для модели Аттестат"""
    queryset = Attestat.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AttestatCreateSerializer
        elif self.action != 'create':
            return AttestatSerializer


class EgeViewSet(viewsets.ModelViewSet):
    """CRUD для модели ЕГЭ"""
    queryset = EGE.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EgeCreateSerializer
        elif self.action != 'create':
            return EgeSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """CRUD для модели Заявка"""
    queryset = Application.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ApplicationCreateSerializer
        elif self.action != 'create':
            return ApplicationSerializer


class EnrolleeViewSet(viewsets.ModelViewSet):
    """Отображение для модели Абитуриент"""
    queryset = Enrollee.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EnrolleeSerializer
        elif self.action != 'create':
            return EnrolleeDetailSerializer


class EgeSubjectViewSet(viewsets.ModelViewSet):
    """Отображение для модели Дисциплина ЕГЭ"""
    queryset = EgeSubject.objects.all()
    serializer_class = EgeSubjectSerializer


class AttestatSubjectViewSet(viewsets.ModelViewSet):
    """Отображение для модели Дисциплина аттестата"""
    queryset = AttestatSubject.objects.all()
    serializer_class = AttestatSubjectSerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    """Отображение для модели Специальность"""
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class FacultyViewSet(viewsets.ModelViewSet):
    """Отображение для модели Факультет"""
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


"""Запросы к курсовой работе"""


class Query1(APIView):
    """Список абитуриентов, подавших заявление на заданную специальность"""

    def get(self, request):
        specialty = request.GET.get('specialty')
        enrollee_list = Application.objects.filter(specialty=specialty)
        serializer = ApplicationSerializer(enrollee_list, many=True)
        return Response({'result': serializer.data})


class Query2(APIView):
    """Количество абитуриентов, подавших заявления на каждую специальность"""

    def get(self, request):
        results = Application.objects.values('specialty', 'form').order_by('specialty').annotate(Count('enrollee'))
        return Response({'result': results})


class Query3(APIView):
    """Количество абитуриентов на базе 9 и 11 классов, поступающих на бюджет (или контракт)."""

    def get(self, request):
        results = Application.objects.values('form').order_by('form').annotate(Count('enrollee'))
        return Response({'result': results})


class Query4(APIView):
    """Общее количество поданных заявлений ежедневно"""

    def get(self, request):
        results = Application.objects.values('date').order_by('date').annotate(Count('enrollee'))
        return Response({'result': results})

# Create your views here.
