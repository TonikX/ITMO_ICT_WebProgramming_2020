from rest_framework import serializers
from .models import JobSeeker, Vacancy, Resume, Experience, Profession, Employer


class JobSeekerListSerializer(serializers.ModelSerializer):
    """Список соискателей"""

    class Meta:
        model = JobSeeker
        fields = '__all__'


# class ExpirienceDetailSerializer(serializers.ModelSerializer):
#     """Опыт работы"""
#
#     class Meta:
#         model = Experience
#         fields = "__all__"


class ResumeDetailSerializer(serializers.ModelSerializer):
    """Резюме"""

    class Meta:
        model = Resume
        fields = "__all__"


class JobSeekerDetailSerializer(serializers.ModelSerializer):
    """Соискатель"""
    resume = ResumeDetailSerializer()

    class Meta:
        model = JobSeeker
        fields = "__all__"


class VacancyListSerializer(serializers.ModelSerializer):
    """Списов активных вакансий"""

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Vacancy
        fields = ("id", "profession", "salary")


class VacancyDetailSerializer(serializers.ModelSerializer):
    """Вакансия"""
    RANK_TYPES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
    ]

    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)
    # education = serializers.SlugRelatedField(slug_field='education', read_only=True)
    employer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rank = serializers.ChoiceField(choices=RANK_TYPES, source='get_rank_display')
    education = serializers.ChoiceField(choices=EDUCATION_TYPES, source='get_education_display')

    class Meta:
        model = Vacancy
        fields = "__all__"


class EmployerListSelializer(serializers.ModelSerializer):
    """Список работодателей"""

    class Meta:
        model = Employer
        fields = ("id", "name", "surname", "second_name", "firm")


class EmployerDetailSelializer(serializers.ModelSerializer):
    """Работодатель"""

    class Meta:
        model = Employer
        fields = "__all__"



