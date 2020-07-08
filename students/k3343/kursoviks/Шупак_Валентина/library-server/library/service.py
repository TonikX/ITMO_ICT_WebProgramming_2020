from django_filters import rest_framework as filters
from .models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    """Фильтрация книг по названию, автору и шифру"""
    author = CharFilterInFilter(field_name='author', lookup_expr='in')
    cipher = CharFilterInFilter(field_name='cipher', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Book
        fields = ['author', 'cipher', 'name']
