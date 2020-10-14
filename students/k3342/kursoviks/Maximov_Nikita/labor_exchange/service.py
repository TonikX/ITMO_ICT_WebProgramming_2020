from django_filters import rest_framework as filters
from .models import Vacancy, Course, CourseCertificate


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class VacancyFilter(filters.FilterSet):
    """Фильтрация по """
    status = CharFilterInFilter(field_name='status', lookup_expr='in')
    education = CharFilterInFilter(field_name='education', lookup_expr='in')
    profession = CharFilterInFilter(field_name='profession', lookup_expr='in')
    types = CharFilterInFilter(field_name='type', lookup_expr='in')
    work_experience = filters.RangeFilter()
    salary = filters.RangeFilter()

    class Meta:
        model = Vacancy
        fields = ['status', 'education', 'profession', 'type', 'work_experience', 'salary']


class CourseFilter(filters.FilterSet):
    """Фильтрация по """
    profession = CharFilterInFilter(field_name='profession', lookup_expr='in')

    class Meta:
        model = Course
        fields = ['profession']


class CourseCertificateFilter(filters.FilterSet):
    """Фильтрация по """
    course = CharFilterInFilter(field_name='', lookup_expr='in')

    class Meta:
        model = CourseCertificate
        fields = ['course']