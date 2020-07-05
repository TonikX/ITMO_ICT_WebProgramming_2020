from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import *
from .serializers import *


class CreateClientView(generics.CreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class GetClientsView(generics.ListAPIView):
	queryset = Client.objects.all()
	serializer_class = GetClientSerializer


class CreateCompanyView(generics.CreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class GetCompaniesView(generics.ListAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class CreateProductView(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class GetProductsView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class GetProductView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class CreateRequestView(generics.CreateAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer


class CreatePaymentView(generics.CreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer


class GetPaymentsView(generics.ListAPIView):
	serializer_class = GetPaymentSerializer

	def get_queryset(self):
		queryset = Payment.objects.all()

		user = self.request.query_params.get('username', None)
	
		if user:
			queryset = queryset.filter(Q(request__client__user__username=user) | Q(request__executor__user__username=user))

		return queryset


class GetPaymentView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Payment.objects.all()
	serializer_class = GetPaymentSerializer


class GetServicesView(generics.ListAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer


class GetServiceView(generics.RetrieveAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer


class GetRequestsView(generics.ListAPIView):
	serializer_class = RequestSerializer

	def get_queryset(self):
		queryset = Request.objects.all()

		user = self.request.query_params.get('username', None)
	
		if user:
			queryset = queryset.filter(Q(client__user__username=user) | Q(executor__user__username=user))

		return queryset


class GetRequestView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer


class GetServiceForRequestView(generics.ListAPIView):
	serializer_class = GetServiceForRequestSerializer

	def get_queryset(self):
		queryset = ServiceForRequest.objects.all()

		user = self.request.query_params.get('username', None)

		# admin filters params
		state = self.request.query_params.get('state', None)
		service = self.request.query_params.get('service', None)
		from_date = self.request.query_params.get('from_date', None)
		to_date = self.request.query_params.get('to_date', None)
		employee = self.request.query_params.get('employee', None)
		client = self.request.query_params.get('client', None)
	
		if user:
			queryset = queryset.filter(Q(request__client__user__username=user) | Q(request__executor__user__username=user))

		if state:
			queryset = queryset.filter(request__state=state)

		if service:
			queryset = queryset.filter(service=service)

		if from_date:
			queryset = queryset.filter(request__date__gte=from_date)

		if to_date:
			queryset = queryset.filter(request__date__lte=to_date)

		if employee:
			queryset = queryset.filter(request__executor=employee)

		if client:
			queryset = queryset.filter(request__client=client)

		return queryset


class CreateServiceForRequestView(generics.CreateAPIView):
	queryset = ServiceForRequest.objects.all()
	serializer_class = ServiceForRequestSerializer


class IsClientView(generics.ListAPIView):
	serializer_class = GetClientSerializer

	def get_queryset(self):
		queryset = Client.objects.all()

		username = self.request.query_params.get('username', None)

		if username:
			queryset = queryset.filter(user__username=username)

		return queryset


class IsEmployeeView(generics.ListAPIView):
	serializer_class = GetEmployeeSerializer

	def get_queryset(self):
		queryset = Employee.objects.all()

		username = self.request.query_params.get('username', None)

		if username:
			queryset = queryset.filter(user__username=username)

		return queryset
