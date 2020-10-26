from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'id']


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Route
		fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
	plane_type = serializers.CharField(source='get_plane_type_display')
	company = CompanySerializer()
	class Meta:
		model = Plane
		fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
	company = CompanySerializer()
	class Meta:
		model = Employees
		fields = '__all__'


class FlightsSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	date = serializers.DateField()
	route = RouteSerializer()
	plane = PlaneSerializer()


class FlightTeamSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	epmloyee = EmployeesSerializer()
	flight = FlightsSerializer()


class TransitPointsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    action = serializers.CharField(source='get_action_display')
    point = serializers.CharField()
    route = RouteSerializer()


class TicketsSerializer(serializers.ModelSerializer):
	state = serializers.CharField(source='get_state_display')
	flight = FlightsSerializer()

	class Meta:
		model = Tickets
		fields = '__all__'


class ChallengersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Challengers
		fields = '__all__'

	def create(self, validated_data):
		return Challengers.objects.create(**validated_data)


class UserTicketSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	flight = FlightsSerializer()

	class Meta:
		model = UserTickets
		fields = '__all__'


class CreateUserTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserTickets
		fields = '__all__'
