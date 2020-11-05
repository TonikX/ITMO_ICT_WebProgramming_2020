from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class LibrarianListView(generics.ListAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class VisitorListView(generics.ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OwnershipListView(generics.ListAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AccessoryListView(generics.ListAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class RentListView(generics.ListAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AddRentView(generics.CreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AddOwnershipView(generics.CreateAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


"""
class TestListView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly
    def get_queryset(self):
        queryset = TestModel.objects.all()
        params = self.request.query_params
        name = params.get('name', None)
        desc = params.get('desc', None)
        if name:
            queryset = queryset.filter(name=name)
        if desc:
            queryset = queryset.filter(desc=desc)
        return queryset"""
