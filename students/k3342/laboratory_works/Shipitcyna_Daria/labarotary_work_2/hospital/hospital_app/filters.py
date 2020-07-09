from django_filters import rest_framework as filters
from .models import *

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class OrderFilter(filters.FilterSet):
    doctor = CharFilterInFilter(field_name="record__doctor__surname", lookup_expr="in")
    date = filters.DateFilter()

    class Meta:
        model = Appointment
        fields = ['record__doctor__surname', 'date']