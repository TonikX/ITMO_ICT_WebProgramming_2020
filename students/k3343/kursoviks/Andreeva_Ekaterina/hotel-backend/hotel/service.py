from django_filters import rest_framework as filters
from .models import Cleaning


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CleaningFilter(filters.FilterSet):
    """Фильтрация графика уборки по дню недели, сотруднику и этажу"""
    servant = CharFilterInFilter(field_name='servant', lookup_expr='in')
    floor = CharFilterInFilter(field_name='floor', lookup_expr='in')
    day = CharFilterInFilter(field_name='day', lookup_expr='in')

    class Meta:
        model = Cleaning
        fields = ['servant', 'floor', 'day']
