from django_filters import rest_framework as filters
from .models import Order, Client


class ClientFilter(filters.FilterSet):
    age = filters.RangeFilter()

    class Meta:
        model = Client
        fields = ['age']


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class OrderFilter(filters.FilterSet):
    driver = CharFilterInFilter(field_name="driver__name", lookup_expr="in")
    data = filters.DateFilter()

    class Meta:
        model = Order
        fields = ['driver__name', 'data']
