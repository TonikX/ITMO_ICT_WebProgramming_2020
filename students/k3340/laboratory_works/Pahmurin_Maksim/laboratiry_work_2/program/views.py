from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Students
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .service import StudentFilter


# Create your views here.
class StudentsListCreateView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentListSerializer
        else:
            return StudentCreateSerializer


class StudentsListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.AllowAny]


class StudentsDetailView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer


class StudentsDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.IsAdminUser]


class SheduleListCreateView(generics.ListCreateAPIView):
    queryset = Shedule.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SheduleSerializer
        else:
            return SheduleCreateSerializer


class TeachersUpdateView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherListSerializer


class StudentsUpdateView(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentCreateSerializer


class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherListSerializer


class SubjectsListView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectListSerializer


class SheduleDeleteView(generics.DestroyAPIView):
    queryset = Shedule.objects.all()
    serializer_class = SheduleSerializer
    permission_classes = [permissions.AllowAny]


class StudentsDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.AllowAny]


class TeachersDeleteView(generics.DestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherListSerializer
    permission_classes = [permissions.AllowAny]


class RecordListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecordListSerializer
        else:
            return RecordCreateSerializer


class TeachersViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherListSerializer

    def filter_queryset(self, queryset):
        for k, v in self.request.query_params.items():
            if k == "cursor":
                continue
            queryset = queryset.filter(**{k: v})
        return queryset


class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentListSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer





