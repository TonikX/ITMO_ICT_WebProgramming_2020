from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class EnrolleeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enrollee
		fields = '__all__'
		depth = 5


class SpecSerializer(serializers.ModelSerializer):
	class Meta:
		model = Spec
		fields = '__all__'
		depth = 5


class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Application
		fields = '__all__'
		depth = 5


class CreateEnrolleeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enrollee
		fields = '__all__'


class CreateApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Application
		fields = '__all__'
