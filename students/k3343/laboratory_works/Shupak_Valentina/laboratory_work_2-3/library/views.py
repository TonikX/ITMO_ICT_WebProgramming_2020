from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
from django.db.models import Count, Avg
from datetime import timedelta
from .models import Book, ReadingRoom, Reader, BookPlace, TakingBook
from .serializers import BookSerializer, ReadingRoomSerializer,  ReaderSerializer, BookPlaceSerializer, \
    TakingBookSerializer, BookCreateSerializer, ReaderCreateSerializer, BookPlaceCreateSerializer, \
    TakingBookCreateSerializer, BookUpdateSerializer, BookPlaceUpdateSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Отображение для модели Книга"""
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return BookCreateSerializer
        elif self.action == 'update':
            return BookUpdateSerializer
        elif self.action == 'destroy':
            return BookSerializer
        elif self.action == 'list':
            return BookSerializer
        elif self.action == 'retrieve':
            return BookSerializer


class ReadingRoomViewSet(viewsets.ModelViewSet):
    """Отображение для модели Читальный зал"""
    queryset = ReadingRoom.objects.all()
    serializer_class = ReadingRoomSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    """Отображение для модели Читатель"""
    queryset = Reader.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReaderCreateSerializer
        elif self.action == 'update':
            return ReaderCreateSerializer
        elif self.action == 'destroy':
            return ReaderSerializer
        elif self.action == 'list':
            return ReaderSerializer
        elif self.action == 'retrieve':
            return ReaderSerializer


class BookPlaceViewSet(viewsets.ModelViewSet):
    """Отображение для модели Расположение книги"""
    queryset = BookPlace.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return BookPlaceCreateSerializer
        elif self.action == 'update':
            return BookPlaceUpdateSerializer
        elif self.action == 'destroy':
            return BookPlaceSerializer
        elif self.action == 'list':
            return BookPlaceSerializer
        elif self.action == 'retrieve':
            return BookPlaceSerializer


class TakingBookViewSet(viewsets.ModelViewSet):
    """Отображение для модели Взятие книги"""
    queryset = TakingBook.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TakingBookCreateSerializer
        elif self.action == 'update':
            return TakingBookCreateSerializer
        elif self.action == 'destroy':
            return TakingBookSerializer
        elif self.action == 'list':
            return TakingBookSerializer
        elif self.action == 'retrieve':
            return TakingBookSerializer


"""Запросы к курсовой работе"""


class Query1(APIView):
    """Какие книги закреплены за определенным читателем?"""

    def get(self, request):
        reader = request.GET.get('reader')
        books = Reader.objects.filter(id=reader)
        book = ReaderSerializer(books, many=True)
        return Response({'result': book.data})


class Query5(APIView):
    """Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?"""

    def get(self, request):
        readers = Reader.objects.count()
        primary = Reader.objects.filter(education='Начальное').count()
        secondary_unfinished = Reader.objects.filter(education='Среднее_неоконченное').count()
        secondary = Reader.objects.filter(education='Среднее').count()
        high_unfinished = Reader.objects.filter(education='Высшее_неоконченное').count()
        high = Reader.objects.filter(education='Высшее').count()
        primary_percent = primary/readers
        secondary_unfinished_percent = secondary_unfinished/readers
        secondary_percent = secondary/readers
        high_unfinished_percent = high_unfinished/readers
        high_percent = high/readers
        academic = Reader.objects.filter(academic='True').count()
        non_academic = Reader.objects.filter(academic='False').count()
        academic_percent = academic/readers
        non_academic_percent = non_academic/readers
        return Response({'primary': primary_percent, 'secondary_unfinished': secondary_unfinished_percent,
                         'secondary': secondary_percent, 'high_unfinished': high_unfinished_percent, 'high': high_percent,
                         'academic': academic_percent, 'non_academic': non_academic_percent})


# Create your views here.
