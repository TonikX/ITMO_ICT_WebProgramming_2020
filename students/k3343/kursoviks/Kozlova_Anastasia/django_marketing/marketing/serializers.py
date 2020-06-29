from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.fields import Field

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class GetClientSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user = UserSerializer()

    class Meta:
        model = Client
        fields = '__all__'


class GetEmployeeSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='get_position_display')
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceForRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceForRequest
        fields = '__all__'


class GetRequestSerializer(serializers.ModelSerializer):
    client = GetClientSerializer()
    executor = GetEmployeeSerializer()
    state = serializers.CharField(source='get_state_display')
    product = ProductSerializer()

    class Meta:
        model = Request
        fields = '__all__'


class GetServiceForRequestSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    request = GetRequestSerializer()

    class Meta:
        model = ServiceForRequest
        fields = '__all__'


class GetPaymentSerializer(serializers.ModelSerializer):
    request = GetRequestSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
