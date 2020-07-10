# from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.
class FlightsView(APIView):
	def get(self, request):
		params = request.query_params

		flight_id = params.get('id')
		from_point = params.get('from_point', '')
		to_point = params.get('to_point', '')
		plane_model = params.get('plane_model', '')
		price = params.get('price', 0)
		ticket_left = params.get('tickets_left', 0)
		is_transit = params.get('is_transit', 'yes')

		flights = Flights.objects.all()
		team = FlightTeam.objects.all()
		transit_points = TransitPoints.objects.all()
		tickets = Tickets.objects.all()

		if flight_id:
			flights = flights.filter(id=flight_id)
			team = team.filter(flight=flight_id)
			route_id = flights[0].route.id if len(flights) > 0 else 0
			transit_points = transit_points.filter(route=route_id)
			tickets = tickets.filter(flight=flight_id)

		if from_point or to_point:
			routes = Route.objects.all().filter(Q(from_point=from_point) | Q(to_point=to_point))
			route_ids = [route.id for route in routes]
			flights = flights.filter(route__in=route_ids)
			flight_ids = [flight.id for flight in flights]
			team = team.filter(flight__in=flight_ids)
			transit_points = transit_points.filter(route__in=route_ids)
			tickets = tickets.filter(flight__in=flight_ids)

		if plane_model:
			planes = Plane.objects.all().filter(model=plane_model)
			plane_ids = [plane.id for plane in planes]
			flights = flights.filter(plane__in=plane_ids)
			flight_ids = [flight.id for flight in flights]
			route_ids = [flight.route.id for flight in flights]
			team = team.filter(flight__in=flight_ids)
			transit_points = transit_points.filter(route__in=route_ids)
			tickets = tickets.filter(flight__in=flight_ids)

		if is_transit == 'no':
			route_ids = [point.route.id for point in transit_points]
			routes = Route.objects.all().exclude(id__in=route_ids)
			flights = flights.exclude(route__in=route_ids)
			flight_ids = [flight.id for flight in flights]
			team = team.filter(flight__in=flight_ids)
			transit_points = transit_points.exclude(route__in=route_ids)
			tickets = tickets.filter(flight__in=flight_ids)

		if int(price) > 0:
			tickets = tickets.filter(Q(price__lte=price) & Q(state='2'))
			flight_ids = [ticket.flight.id for ticket in tickets]
			flights = flights.filter(id__in=flight_ids)
			team = team.filter(flight__in=flight_ids)
			route_ids = [flight.route.id for flight in flights]
			transit_points = transit_points.filter(route__in=route_ids)

		if int(ticket_left) > 0:
			tickets = tickets.filter(Q(amount__lte=ticket_left) & Q(state='2'))
			flight_ids = [ticket.flight.id for ticket in tickets]
			flights = flights.filter(id__in=flight_ids)
			team = team.filter(flight__in=flight_ids)
			route_ids = [flight.route.id for flight in flights]
			transit_points = transit_points.filter(route__in=route_ids)

		flights_serializer = FlightsSerializer(flights, many=True)
		team_serializer = FlightTeamSerializer(team, many=True)
		transit_points_serializer = TransitPointsSerializer(transit_points, many=True)
		tickets_serializer = TicketsSerializer(tickets, many=True)

		return Response({
			"flights": flights_serializer.data,
			"transit_points": transit_points_serializer.data,
			"teams": team_serializer.data,
			"tickets": tickets_serializer.data
		})


class ChallengersView(APIView):
	def post(self, request):
		challenger = request.data.get('challenger')
		print("challenger:", challenger)

		serializer = ChallengersSerializer(data=challenger)

		if serializer.is_valid(raise_exception=True):
			challenger_saved = serializer.save()

		return Response({"Success": "Challenger '{}' created succesfully.".format(challenger_saved.last_name)})


class CompaniesView(APIView):
	def get(self, request):
		companies = Company.objects.all()
		companies_serializer = CompanySerializer(companies, many=True)

		return Response({"companies": companies_serializer.data})


class UserTicketView(APIView):
	def get(self, request):
		user_ticket = UserTickets.objects.all()

		params = request.query_params

		user = params.get('user', None)

		if user:
			user_ticket = user_ticket.filter(user__username=user)
		
		user_ticket_serializer = UserTicketSerializer(user_ticket, many=True)

		return Response({"user_ticket": user_ticket_serializer.data})

	def post(self, request):
		user = request.data.get('user')
		flight = request.data.get('flight')

		data = {"user": user, "flight": flight}

		serializer = CreateUserTicketSerializer(data=data)

		if serializer.is_valid(raise_exception=True):
			data_saved = serializer.save()

		return Response({"Success": "User ticket added {}".format(data_saved)})


class GetUserView(APIView):
	def get(self, request):
		user_data = User.objects.all()

		params = request.query_params

		user = params.get('user', None)

		if user:
			user_data = user_data.filter(username=user)

		user_serializer = UserSerializer(user_data, many=True)

		return Response({"user": user_serializer.data})
