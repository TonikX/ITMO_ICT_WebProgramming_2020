from rest_framework import serializers
from .models import JobSeeker, Vacancy


class JobSeekerListSerializer(serializers.ModelSerializer):
    """Список соискателей"""

    class Meta:
        model = JobSeeker
        fields = '__all__'


class VacancyListSerializer(serializers.ModelSerializer):
    """Списов активных вакансий"""

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Vacancy
        fields = ("id", "profession", "salary")

