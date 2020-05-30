from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Dog, Club, User, Show, Registration, Ring, \
    Perform, Grade
from .serializers import DogListSerializer, ClubListSerializer, \
    UserListSerializer, ShowListSerializer, RegistrationListSerializer, \
    RingListSerializer, PerformListSerializer, GradeListSerializer


class DogListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class DogDetailView(generics.RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class ClubListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubListSerializer


class ExpertListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = User.objects.filter(expert=True)
    serializer_class = UserListSerializer


class ShowListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowListSerializer


class RegistrationListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationListSerializer


class RingListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Ring.objects.all()
    serializer_class = RingListSerializer


class PerformListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Perform.objects.all()
    serializer_class = PerformListSerializer


class GradeListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer


