from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import *


class ReadersSerializer(serializers.ModelSerializer):
    """Сериализация читателей"""
    class Meta:
        model = Reader
        fields = ('id', 'library_card', 'name', 'passport_number')


class ReaderSerializer(serializers.ModelSerializer):
    """Сериализация читателя"""

    class Meta:
        model = Reader
        fields = ('id', 'library_card',  'name', 'passport_number', 'date_of_birth',
                  'address', 'phone', 'education', 'academic')


class BooksSerializer(serializers.ModelSerializer):
    """Сериализация книг"""
    class Meta:
        model = Book
        fields = ('id', 'cipher', 'name', 'author')


class BookSerializer(serializers.ModelSerializer):
    """Сериализация книги"""
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'publisher', 'year', 'section', 'cipher')


class PlacesSerializer(serializers.ModelSerializer):
    """Сериализация мест"""
    class Meta:
        model = Place
        fields = "__all__"


class FixUpdSerializer(serializers.ModelSerializer):
    """Сериализатор для открепления книги """
    class Meta:
        model = Fix
        fields = ('id', 'handed')


class FixesSerializer(serializers.ModelSerializer):
    """Сериализация закрепления"""
    book = BooksSerializer(read_only=True)
    reader = ReadersSerializer(read_only=True)

    class Meta:
        model = Fix
        fields = ('id', 'book', 'reader', 'date_fix', 'place')


class FixAddSerializer(serializers.ModelSerializer):
    """Сериализация для добавления закрепления"""

    class Meta:
        model = Fix
        fields = ('book', 'reader', 'place')


class FixReaderSerializer(serializers.ModelSerializer):
    """Сериализация вывода закрепленных книг у читателя"""
    book = BookSerializer()

    class Meta:
        model = Fix
        fields = ('id', 'book', 'date_fix', 'place', 'handed')


class PlaceUpdSerializer(serializers.ModelSerializer):
    """Сериализатор для открепления книги """
    class Meta:
        model = Fix
        fields = ('id', 'place')


class ReadersDateSerializer(serializers.ModelSerializer):
    """Сериализация читателей"""
    class Meta:
        model = Reader
        fields = ('id', 'library_card', 'name', 'date_of_birth')
