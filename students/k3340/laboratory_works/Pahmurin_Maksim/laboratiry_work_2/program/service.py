from django_filters import rest_framework as filters
from .models import Students

class CharFilterInFilters(filters.BaseInFilter, filters.CharFilter):
    pass

class StudentFilter(filters.FilterSet):
    group = CharFilterInFilters(field_name='group__group', lookup_expr='in')

    class Meta:
        model = Students
        fields = ['group']
