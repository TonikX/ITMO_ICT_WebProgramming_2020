from django.shortcuts import render
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

from .models import *
from .serializers import (ReaderSerializer, BooksSerializer, BookSerializer, ReadersSerializer,
                          FixUpdSerializer,  FixesSerializer, FixReaderSerializer, FixAddSerializer,
                          PlacesSerializer, PlaceUpdSerializer, ReadersDateSerializer)


class Readers(APIView):
    """Отображение всех читателей"""

    def get(self, request):
        readers = Reader.objects.all()
        serializers = ReadersSerializer(readers, many=True)
        return Response(serializers.data)


class ReaderOne(APIView):
    """Отображение одного читателя и все взятые им книги на данный момент"""

    def get(self, request):
        id_reader = request.GET.get("reader")
        reader = Reader.objects.filter(id=id_reader)
        reader_serializer = ReaderSerializer(reader, many=True)
        fixes = Fix.objects.filter(reader=id_reader, handed=False)
        book_serializer = FixReaderSerializer(fixes, many=True)
        return Response({"reader": reader_serializer.data, "books": book_serializer.data})


class ReaderAdd(APIView):
    """Добавление читателя"""
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        reader = ReaderSerializer(data=request.data)
        if reader.is_valid():
            reader.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class ReaderDelUpd(viewsets.ModelViewSet):
    """Отображение для модели Взятие книги"""
    queryset = Reader.objects.all()

    def get_serializer_class(self):
        if self.action == 'destroy':
            return ReaderSerializer
        elif self.action == 'update':
            return ReaderSerializer


class Books(APIView):
    """Отображение всех книг"""

    def get(self, request):
        books = Book.objects.all()
        serializers = BooksSerializer(books, many=True)

        return Response(serializers.data)


class BookOne(APIView):
    """Отображение одной книги"""

    def get(self, request):
        id_book = request.GET.get("book")
        book = Book.objects.filter(cipher=id_book)
        serializer = BookSerializer(book, many=True)
        return Response({"book": serializer.data})


class BookAdd(APIView):
    """Добавление книги"""
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class BookDelUpd(viewsets.ModelViewSet):
    """Отображение для модели Взятие книги"""
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'destroy':
            return BookSerializer
        elif self.action == 'update':
            return BookSerializer


class Fixes(APIView):
    """Закрепления"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        fixes = Fix.objects.all()
        serializers = FixesSerializer(fixes, many=True)
        return Response({"data": serializers.data})


class FixAdd(APIView):
    """Добавление закрепления"""
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        fix = FixAddSerializer(data=request.data)
        if fix.is_valid():
            fix.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class FixUpdate(viewsets.ModelViewSet):
    """Отображение обновления заркрепления (открепление книги)"""
    queryset = Fix.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return FixUpdSerializer


class Places(APIView):
    """Места"""

    def get(self, request):
        places = Place.objects.all()
        serializers = PlacesSerializer(places, many=True)
        return Response({"place": serializers.data})


class PlaceOne(APIView):
    """Отображение одного зала и все закрепления в нем"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        id_place = request.GET.get("place")
        place_single = Place.objects.filter(id=id_place)
        serializer = PlacesSerializer(place_single, many=True)
        fixes = Fix.objects.filter(place=id_place, handed=False)
        fixes_serializer = FixesSerializer(fixes, many=True)
        return Response({"place": serializer.data, "fixes": fixes_serializer.data})


class PlaceUpd(viewsets.ModelViewSet):
    """Отображение обновления заркрепления (открепление книги)"""
    queryset = Fix.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return PlaceUpdSerializer
        elif self.action == 'list':
            return PlaceUpdSerializer


class FixFilter(APIView):
    """Отображение фильтрации по дате за месяц"""
    def get(self, request):
        now = datetime.now() - timedelta(days=30)
        fixes = Fix.objects.filter(date_fix__lte=now)
        serializer = FixesSerializer(fixes, many=True)
        return Response({"data": serializer.data})


class ReadersFilter(APIView):
    """Отображение фильтрации по дате рождения (меньше 20 лет)"""
    def get(self, request):
        now = datetime.now() - timedelta(days=365*20)
        readers = Reader.objects.filter(date_of_birth__gte=now)
        serializer = ReadersDateSerializer(readers, many=True)
        return Response({"data": serializer.data})


class EducationFiler(APIView):
    """Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?"""

    def get(self, request):
        readers = Reader.objects.count()
        primary = Reader.objects.filter(education='Начальное общее').count()
        secondary = Reader.objects.filter(education='Среднее общее').count()
        high = Reader.objects.filter(education='Высшее').count()
        primary_percent = (primary/readers) * 100
        secondary_percent = (secondary/readers) * 100
        high_percent = (high/readers) * 100
        academic = Reader.objects.filter(academic='True').count()
        academic_percent = (academic/readers) * 100
        return Response({'primary': primary_percent, 'secondary': secondary_percent, 'high': high_percent,
                         'academic': academic_percent})