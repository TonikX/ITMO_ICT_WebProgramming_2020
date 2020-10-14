from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .service import VacancyFilter, CourseFilter, CourseCertificateFilter
from collections import Counter
from django.db.models import Count, Avg

from .models import Education, Profession, Field, Applicant, Resume, Course, CourseCertificate, Gratuity, Employer, Vacancy, Application
from .serializers import EducationSerializer, ProfessionSerializer, FieldSerializer, ApplicantSerializer,\
    ResumeSerializer, CourseSerializer, CourseCertificateSerializer, GratuitySerializer, EmployerSerializer, \
    VacancySerializer, ApplicationSerializer, VacancyCreateSerializer, VacancyUpdateSerializer, \
    ResumeCreateSerializer, ResumeUpdateSerializer, CourseCertificateCreateSerializer, GratuityCreateSerializer,\
    GratuityUpdateSerializer, ApplicantCreateSerializer, ApplicantUpdateSerializer, CourseCreateSerializer, \
    ApplicationUpdateSerializer, ApplicationDetailSerializer


class EducationViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class FieldViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Applicant.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ApplicantCreateSerializer
        elif self.action == 'update':
            return ApplicantUpdateSerializer
        else:
            return ApplicantSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Resume.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ResumeCreateSerializer
        elif self.action == 'update':
            return ResumeUpdateSerializer
        else:
            return ResumeSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Course.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = CourseFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseCreateSerializer
        elif self.action != 'create':
            return CourseSerializer


class CourseCertificateViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = CourseCertificate.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = CourseCertificateFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseCertificateCreateSerializer
        elif self.action != 'create':
            return CourseCertificateSerializer


class GratuityViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Gratuity.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return GratuityCreateSerializer
        elif self.action == 'update':
            return GratuityUpdateSerializer
        else:
            return GratuitySerializer


class EmployerViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Vacancy.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = VacancyFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return VacancyCreateSerializer
        elif self.action == 'update':
            return VacancyUpdateSerializer
        else:
            return VacancySerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """Отображение для модели """
    queryset = Application.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return ApplicationUpdateSerializer
        elif self.action == 'retrieve':
            return ApplicationDetailSerializer
        else:
            return ApplicationSerializer


class CountCourse(APIView):
    """количество людей на курсе"""

    def get(self, request):
        results = CourseCertificate.objects.values('course').order_by('course').annotate(Count('applicant'))
        return Response({'result': results})
# Create your views here.
