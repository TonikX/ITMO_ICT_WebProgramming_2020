from django_filters import rest_framework as filters
from .models import Timetable


def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TimetableFilter(filters.FilterSet):
    """Фильтрация расписания по дню недели и по классу"""
    klass = CharFilterInFilter(field_name='klass_name', lookup_expr='in')
    day = CharFilterInFilter(field_name='day', lookup_expr='in')

    class Meta:
        model = Timetable
        fields = ['klass_name', 'day']