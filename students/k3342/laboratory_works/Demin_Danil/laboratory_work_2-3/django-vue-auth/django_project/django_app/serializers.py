from rest_framework import serializers
from .models import *


class ChickenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chicken
		fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Worker
		fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chicken
		fields = '__all__'

class CageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cage
		fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'
