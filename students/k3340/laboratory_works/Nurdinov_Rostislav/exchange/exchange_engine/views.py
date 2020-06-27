from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobSeeker, Vacancy
from .serializers import JobSeekerListSerializer, VacancyListSerializer


class JobSeekerListView(APIView):
    """Вывод списка соискателей"""
    def get(self, request):
        jobseeker = JobSeeker.objects.all()
        serializer = JobSeekerListSerializer(jobseeker, many=True)
        return Response(serializer.data)


class VacancyListView(APIView):
    """Вывод активных вакансий"""
    def get(self, request):
        vacancy = Vacancy.objects.filter(status=True)
        serializer = VacancyListSerializer(vacancy, many=True)
        return Response(serializer.data)

