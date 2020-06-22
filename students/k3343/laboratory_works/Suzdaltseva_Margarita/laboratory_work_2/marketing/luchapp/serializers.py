from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class NewCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    company_type = serializers.CharField(source='get_company_type_display')
    class Meta:
        model = Company
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(source="get_service_type_display")
    class Meta:
        model = Service
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class NewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    position = serializers.CharField(source="get_position_display")

    class Meta:
        model = Employee
        fields = '__all__'


class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    #status = serializers.CharField(source="get_status_display")
    service = ServiceSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Request
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


