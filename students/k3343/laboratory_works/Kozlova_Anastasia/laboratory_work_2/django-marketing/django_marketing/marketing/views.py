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


class CreateCompanyView(generics.CreateAPIView):
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
	queryset = Request.objects.all()
	serializer_class = PaymentSerializer


class GetPaymentView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Request.objects.all()
	serializer_class = PaymentSerializer


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
		client = self.request.query_params.get('client', None)
		executor = self.request.query_params.get('executor', None)
	
		if client or executor:
			queryset = Request.objects.filter(Q(client=client) | Q(executor=executor))

		return queryset


class GetRequestView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer


class CreateServiceForRequestView(generics.CreateAPIView):
	queryset = ServiceForRequest.objects.all()
	serializer_class = ServiceForRequestSerializer
