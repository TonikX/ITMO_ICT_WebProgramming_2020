from rest_framework import viewsets, permissions
#from django_filters.rest_framework import DjangoFilterBackend
#from .service import TimetableFilter

from .models import Teacher, Timetable, Nclass, Children, Room, Subject, Grade
from . import serializers


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TeacherListSerializer
        elif self.action == 'update':
            return serializers.TeacherDetailSerializer
        elif self.action == 'create':
            return serializers.TeacherAddSerializer
        elif self.action != 'list':
            return serializers.TeacherDetailSerializer


class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ChildrenListSerializer
        elif self.action == 'update':
            return serializers.ChildrenSerializer
        elif self.action == 'create':
            return serializers.ChildrenAddSerializer
        elif self.action != 'list':
            return serializers.ChildrenDetailSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.GradeCreateSerializer
        elif self.action != 'create':
            return serializers.GradeSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
#    filter_backends = (DjangoFilterBackend,
#                      )
#    filterset_class = TimetableFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TimetableSerializer
        elif self.action == 'retrieve':
            return serializers.TimetableSerializer
        elif self.action == 'update':
            return serializers.TimetableSerializer
        elif self.action == 'create':
            return serializers.TimetableAddSerializer


class NclassViewSet(viewsets.ModelViewSet):
    queryset = Nclass.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.NclassSerializer
        elif self.action == 'create':
            return serializers.NclassAddSerializer
        elif self.action != 'list':
            return serializers.NclassDetailSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RoomSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SubjectSerializer

# Create your views here.
