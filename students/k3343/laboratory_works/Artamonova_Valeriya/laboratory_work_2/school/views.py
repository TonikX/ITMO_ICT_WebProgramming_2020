from rest_framework import generics, permissions, viewsets, renderers
from django_filters.rest_framework import DjangoFilterBackend
from .service import TimetableFilter

from .models import Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade
from .serializers import (TeacherSerializer, TeacherDetailSerializer, TeacherAddSerializer, PupilSerializer,
                          PupilDetailSerializer, GradeCreateSerializer, PupilAddSerializer, TimetableSerializer,
                          TimetableAddSerializer, KlassSerializer, SubjectSerializer, CabinetSerializer,
                          KlassDetailSerializer, KlassAddSerializer, GradeSerializer)


class TeacherViewSet(viewsets.ModelViewSet):
    """CRUD для модели Учитель"""
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherSerializer
        elif self.action == 'update':
            return TeacherDetailSerializer
        elif self.action == 'create':
            return TeacherAddSerializer
        elif self.action !='list':
            return TeacherDetailSerializer


class PupilViewSet(viewsets.ModelViewSet):
    """CRUD для модели Ученик"""
    queryset = Pupil.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PupilSerializer
        elif self.action == 'update':
            return PupilSerializer
        elif self.action == 'create':
            return PupilAddSerializer
        elif self.action !='list':
            return PupilDetailSerializer


class GradeViewSet(viewsets.ModelViewSet):
    """CRUD для модели Оценка"""
    queryset = Grade.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return GradeCreateSerializer
        elif self.action != 'create':
            return GradeSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    """CRUD для модели Расписание"""
    queryset = Timetable.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = TimetableFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TimetableSerializer
        elif self.action == 'retrieve':
            return TimetableSerializer
        elif self.action == 'update':
            return TimetableSerializer
        elif self.action == 'create':
            return TimetableAddSerializer


class KlassViewSet(viewsets.ModelViewSet):
    """CRUD для модели Класс"""
    queryset = Klass.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return KlassSerializer
        elif self.action == 'create':
            return KlassAddSerializer
        elif self.action !='list':
            return KlassDetailSerializer


class CabinetViewSet(viewsets.ModelViewSet):
    """Отображение для модели Кабинет"""
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """Отображение для модели Предмет"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
