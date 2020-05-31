from rest_framework import generics, permissions, viewsets, renderers
#from rest_framework.response import Response
#from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .service import get_client_ip, TimetableFilter

from .models import UserProfile,Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade
from .serializers import (TeacherSerializer, TeacherDetailSerializer, TeacherAddSerializer, PupilSerializer,
                          PupilDetailSerializer, GradeCreateSerializer, PupilAddSerializer, TimetableSerializer,
                          TimetableAddSerializer, KlassSerializer, SubjectSerializer, CabinetSerializer,
                          KlassDetailSerializer, KlassAddSerializer)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherSerializer
        elif self.action == "create":
            return TeacherAddSerializer
        elif self.action !="list":
            return TeacherDetailSerializer


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PupilSerializer
        elif self.action == "create":
            return PupilAddSerializer
        elif self.action !="list":
            return PupilDetailSerializer


class GradeCreateView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = TimetableFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TimetableSerializer
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
            return TimetableAddSerializer


class KlassViewSet(viewsets.ModelViewSet):
    queryset = Klass.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return KlassSerializer
        elif self.action == 'create':
            return KlassAddSerializer
        elif self.action !="list":
            return KlassDetailSerializer


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
