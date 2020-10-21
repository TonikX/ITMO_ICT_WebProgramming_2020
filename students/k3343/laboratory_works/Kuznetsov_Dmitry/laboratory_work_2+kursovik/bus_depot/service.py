from django_filters import rest_framework as filters
from .models import Schedule, Journal, Driver


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ScheduleFilter(filters.FilterSet):
    """Фильтрация расписания"""
    day = CharFilterInFilter(field_name='day', lookup_expr='in')
    driver = CharFilterInFilter(field_name='driver', lookup_expr='in')
    bus = CharFilterInFilter(field_name='bus', lookup_expr='in')
    route = CharFilterInFilter(field_name='route', lookup_expr='in')

    class Meta:
        model = Schedule
        fields = ['day', 'driver', 'bus', 'route']


class JournalFilter(filters.FilterSet):
    """Фильтрация журнала"""
    date = CharFilterInFilter(field_name='date', lookup_expr='in')
    status = CharFilterInFilter(field_name='status', lookup_expr='in')

    class Meta:
        model = Journal
        fields = ['date', 'status']


class DriverFilter(filters.FilterSet):
    """Фильтрация водителей"""
    driver_class = CharFilterInFilter(field_name='driver_class', lookup_expr='in')

    class Meta:
        model = Driver
        fields = ['driver_class']