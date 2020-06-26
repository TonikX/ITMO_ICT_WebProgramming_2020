from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q
from django.contrib.auth import get_user_model

from .serializers import *
from .models import *

# Requests
class CreateRequestView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = CreateRequestSerializer


class GetRequestView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class GetRequestsView(generics.ListAPIView):
    serializer_class = RequestSerializer
    def get_queryset(self):
        queryset = Request.objects.all()
        user = self.request.query_params.get('user', None)
        #client = self.request.query_params.get('client', None)
        #employee = self.request.query_params.get('employee', None)
        #if client:
        #    queryset = queryset.filter(client=client)
        if user:
            queryset = queryset.filter(Q(employee__user__username=user) | Q(client__user__username=user))
        return queryset


class AdminFilterView(generics.ListAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        params = self.request.query_params

        service = params.get('service', None)
        client = params.get('client', None)
        employee = params.get('employee', None)
        status = params.get('status', None)
        after = params.get('after', None)
        before = params.get('before', None)

        if service:
            queryset = queryset.filter(service__id=service)

        if client:
            queryset = queryset.filter(client__id=client)

        if employee:
            queryset = queryset.filter(employee__id=employee)

        if status:
            queryset = queryset.filter(status=status)

        if after:
            queryset = queryset.filter(date__date__gte=after)

        if before:
            queryset = queryset.filter(date__date__lte=before)

        return queryset


# Company & Client
class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = NewClientSerializer


class CreateCompanyView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = NewCompanySerializer


class GetClientView(generics.ListAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        params = self.request.query_params
        user = params.get('user', None)
        queryset = Client.objects.all()
        if user:
            queryset = queryset.filter(user__username=user)
        return queryset


# All employees & clients
class GetClientsView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GetEmployeesView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Check if employee is head
class GetHeadView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        params = self.request.query_params
        user = params.get('user', None)
        queryset = Employee.objects.all()
        if user:
             queryset = queryset.filter(Q(user__username=user) & Q(position='h'))
        return queryset


# Payments
class CreatePaymentView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class GetPaymentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class GetPaymentsView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    def get_queryset(self):
        queryset = Payment.objects.all()
        params = self.request.query_params
        req = params.get('req', None)
        if req:
            queryset = queryset.filter(request__id=req)
        return queryset


# Services
class GetServiceView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GetServicesView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Products
class GetProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.all()
        params = self.request.query_params
        req = params.get('req', None)
        if req:
            queryset = queryset.filter(request__id=req)
        return queryset


