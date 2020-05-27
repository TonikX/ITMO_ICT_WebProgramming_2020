from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *


# Create your views here.
class FlightsView(generics.ListAPIView):
	serializer_class = FlightSerializer

	def get_queryset(self):
		queryset = Flight.objects.all()

		query_params = self.request.query_params

		arrival = query_params.get('arrival', None)
		departure = query_params.get('departure', None)
		is_transit = query_params.get('is_transit', None)
		tickets_saled = query_params.get('tickets', None)
		price = query_params.get('price', None)

		is_transit = True is is_transit else False

		queryset = queryset.filter(arrival_point=arrival) if arrival else queryset
		queryset = queryset.filter(departure_point=departure) if departure else queryset
		queryset = queryset.filter(is_transit=is_transit) if is_transit not None else queryset
		queryset = queryset.filter(saled_tickets_amount__lte=tickets_saled) if tickets_saled else queryset
		queryset = queryset.filter(price__lte=price) if price else queryset

		return queryset


class FlightView(generics.RetrieveAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class CompanysView(generics.ListAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class CompanyView(generics.RetrieveAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class PlanesView(generics.ListAPIView):
	queryset = Plane.objects.all()
	serializer_class = PlaneSerializer


class PlaneView(generics.RetrieveAPIView):
	queryset = Plane.objects.all()
	serializer_class = PlaneSerializer


class TransitLandingsView(generics.ListAPIView):
	queryset = TransitLanding.objects.all()
	serializer_class = TransitLandingSerializer


class TransitLandingView(generics.RetrieveAPIView):
	queryset = TransitLanding.objects.all()
	serializer_class = TransitLandingSerializer


class ArrivalDeparturesView(generics.ListAPIView):
	serializer_class = ArrivalDepartureSerializer

	def get_queryset(self):
		queryset = ArrivalDeparture.objects.all()

		query_params = self.request.query_params

		plane = query_params.get('plane', None)

		queryset = queryset.filter(plane__plane_model=plane) if plane else queryset

		return queryset


class ArrivalDepartureView(generics.RetrieveAPIView):
	queryset = ArrivalDeparture.objects.all()
	serializer_class = ArrivalDepartureSerializer


class WorkersView(generics.ListAPIView):
	queryset = Worker.objects.all()
	serializer_class = WorkerSerializer


class WorkerView(generics.RetrieveAPIView):
	queryset = Worker.objects.all()
	serializer_class = WorkerSerializer


class CrewsView(generics.ListAPIView):
	queryset = Crew.objects.all()
	serializer_class = CrewSerializer


class CrewView(generics.RetrieveAPIView):
	queryset = Crew.objects.all()
	serializer_class = CrewSerializer


class ChallengerView(generics.CreateAPIView):
	queryset = Challenger.objects.all()
	serializer_class = ChallengerSerializer
