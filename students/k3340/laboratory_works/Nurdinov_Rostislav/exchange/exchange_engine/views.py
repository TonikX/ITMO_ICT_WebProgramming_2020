from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import JobSeeker, Vacancy, Resume
from .serializers import *


class JobSeekerListView(generics.ListAPIView):
    """Вывод списка соискателей"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListSerializer


class JobSeekerDetailView(generics.RetrieveAPIView):
    """Вывод списка соискателей"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerDetailSerializer


# class JobResumeListView(APIView):


class VacancyListView(APIView):
    """Вывод активных вакансий"""
    def get(self, request):
        vacancies = Vacancy.objects.filter(status=True)
        serializer = VacancyListSerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyDetailView(APIView):
    """Вывод активных вакансий"""
    def get(self, request, pk):
        vacancy = Vacancy.objects.get(id=pk)
        serializer = VacancyDetailSerializer(vacancy)
        return Response(serializer.data)


class EmployerListView(APIView):
    """Вывод всех работодателей"""
    def get(self, request):
        employers = Employer.objects.all()
        serializer = EmployerListSelializer(employers, many=True)
        return Response(serializer.data)


class EmployerDetailView(APIView):
    """Вывод работодателя"""
    def get(self, request, pk):
        employer = Employer.objects.get(id=pk)
        serializer = EmployerDetailSelializer(employer)
        return Response(serializer.data)

