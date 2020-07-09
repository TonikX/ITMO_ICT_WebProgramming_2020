from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

from .models import JobSeeker, Vacancy, Resume, Application
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ResumeListView(generics.ListAPIView):
    """Вывод списка соискателей"""
    # queryset = Resume.objects.all()
    serializer_class = ResumeListSerializer

    def get_queryset(self):
        queryset = Resume.objects.all()
        params = self.request.query_params

        jobseeker = params.get('jobseeker', None)

        if jobseeker:
            queryset = queryset.filter(jobseeker=jobseeker)

        return queryset
    # permission_classes = [permissions.IsAuthenticated]


class ResumeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод соискателея"""
    queryset = Resume.objects.all()
    serializer_class = ResumeDetailSerializer

    # permission_classes = [permissions.IsAuthenticated]


class ResumeCreateView(generics.CreateAPIView):
    """Создание соискателя"""
    queryset = Resume.objects.all()
    serializer_class = ResumeCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        jobseeker = JobSeeker.objects.get(user=self.request.user)
        print(jobseeker)
        print(self.request.user.is_staff)
        serializer.save(jobseeker=jobseeker, **self.kwargs)


class JobSeekerListView(generics.ListAPIView):
    """Вывод списка соискателей"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListSerializer
    # permission_classes = [permissions.IsAuthenticated]


class JobSeekerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод соискателея"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerDetailSerializer


class JobSeekerCreateView(generics.CreateAPIView):
    """Создание соискателя"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, **self.kwargs)


class VacancyListView(generics.ListAPIView):
    """Вывод списка вакансий"""
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        params = self.request.query_params

        profession = params.get('profession', None)
        from_s = params.get('from_s', None)
        to_s = params.get('to_s', None)
        min_exp = params.get('min_exp', None)

        if profession:
            queryset = queryset.filter(profession=profession)

        if from_s and to_s:
            queryset = queryset.filter(salary__range=(from_s, to_s))
        elif from_s:
            queryset = queryset.filter(salary__gte=from_s)
        elif to_s:
            queryset = queryset.filter(salary__lte=to_s)

        if min_exp:
            queryset = queryset.filter(min_exp__lte=min_exp)

        return queryset


class VacancyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод вакансии"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class VacancyCreateView(generics.CreateAPIView):
    """Создание вакансии"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class ProfessionListView(generics.ListAPIView):
    """Вывод списка профессий"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer


class ProfessionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод профессии"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionDetailSerializer


class ProfessionCreateView(generics.CreateAPIView):
    """Создание професии"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionCreateSerializer


class EmployerListView(generics.ListAPIView):
    """Вывод списка работодателей"""
    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод работодателя"""
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class EmployerCreateView(generics.CreateAPIView):
    """Создание работодателя"""
    queryset = Employer.objects.all()
    serializer_class = EmployerCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class ExperienceListView(APIView):
    """Список опытов работы"""

    def get(self, request, pk):
        queryset = Experience.objects.filter(resume=pk)
        serializer = ExperienceListSerializer(queryset, many=True)
        return Response(serializer.data)
    # queryset = Experience.objects.all()
    # serializer_class = ExperienceListSerializer


class ExperienceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Опыт работы"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceDetailSerializer


class ExperienceCreateView(generics.CreateAPIView):
    """Создания опыта работы"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceCreateSerializer


class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer


class ApplicationRetrieveUpdateDeleteView(APIView):
    """Опыт работы"""
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer
    # def get(self, request, pk):
    #     vacancy = Vacancy.objects.get(id=pk)
    #     queryset = Application.objects.get(vacancy=vacancy)
    #     serializer = Application(queryset)
    #     return Response(serializer.data)


class ApplicationCreateView(generics.CreateAPIView):
    """Создания опыта работы"""
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer

    def perform_create(self, serializer):
        jobseeker = JobSeeker.objects.get(user=self.request.user)
        resume = Resume.objects.get(jobseeker=jobseeker)
        print(self.args)
        vacancy = Vacancy.objects.get(id=self.args['vacancy_id'])
        serializer.save(resume=resume, vacancy=vacancy, **self.kwargs)
