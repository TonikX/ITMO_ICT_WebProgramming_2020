from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CageListView(generics.ListAPIView):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ChickenListView(generics.ListAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AddChickenView(generics.CreateAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AddReportView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
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
