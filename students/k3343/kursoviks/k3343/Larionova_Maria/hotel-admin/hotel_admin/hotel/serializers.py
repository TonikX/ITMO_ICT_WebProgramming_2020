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


class CreateRoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
	room_type = serializers.CharField(source='get_room_type_display')
	#room_state = serializers.CharField(source='get_room_state_display')

	class Meta:
		model = Room
		fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'


class CreateClientRoomSerializer(serializers.ModelSerializer):
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


class ChallengerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Challengers
		fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Request
		fields = '__all__'


class GetRequestSerializer(serializers.ModelSerializer):
	challenger = ChallengerSerializer()
	administrator = EmployeeSerializer()
	state = serializers.CharField(source='get_state_display')

	class Meta:
		model = Request
		fields = '__all__'
