from django_filters import rest_framework as filters
from .models import *


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MountainFilter(filters.FilterSet):
    height = filters.RangeFilter()

    class Meta:
        model = Mountain
        fields = ['height', ]
