from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Floor
		fields = '__all__'


class NewRoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'


class NewClientRoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClientRoom
		fields = '__all__'


class ClientRoomSerializer(serializers.ModelSerializer):
	client = ClientSerializer()
	room = RoomSerializer()

	class Meta:
		model = ClientRoom
		fields = '__all__'


class CleaningSerializer(serializers.ModelSerializer):
	employee = EmployeeSerializer()
	floor = FloorSerializer()

	class Meta:
		model = Cleaning
		fields = '__all__'


class NewCleaningSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cleaning
		fields = '__all__'
