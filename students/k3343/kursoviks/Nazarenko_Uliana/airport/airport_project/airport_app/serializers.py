from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta():
		model = User
		fields = ['username', 'email', 'id']


class CompanySerializer(serializers.ModelSerializer):
	class Meta():
		model = Company
		fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
	class Meta():
		model = Plane
		fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
	class Meta():
		model = Flight
		fields = '__all__'


class TransitLandingSerializer(serializers.ModelSerializer):
	class Meta():
		model = TransitLanding
		fields = '__all__'


class ArrivalDepartureSerializer(serializers.ModelSerializer):
	company = CompanySerializer()
	flight = FlightSerializer()
	plane = PlaneSerializer()

	class Meta():
		model = ArrivalDeparture
		fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
	class Meta():
		model = Worker
		fields = '__all__'


class ChallengerSerializer(serializers.ModelSerializer):
	class Meta():
		model = Challenger
		fields = '__all__'


class GetChallengerSerializer(serializers.ModelSerializer):
	company = CompanySerializer()
	position = serializers.CharField(source='get_position_display')

	class Meta():
		model = Challenger
		fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
	class Meta():
		model = Crew
		fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	flight = FlightSerializer()
	class Meta():
		model = Ticket
		fields = '__all__'


class AddTicketSerializer(serializers.ModelSerializer):
	class Meta():
		model = Ticket
		fields = '__all__'
