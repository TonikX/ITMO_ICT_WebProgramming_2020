from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *


class NewFloorView(generics.CreateAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class GetFloorView(generics.RetrieveAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class AllFloorView(generics.ListAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class NewRoomView(generics.CreateAPIView):
	queryset = Room.objects.all()
	serializer_class = NewRoomSerializer


class GetRoomView(generics.RetrieveUpdateAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class AllRoomView(generics.ListAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class NewClientView(generics.CreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class GetClientView(generics.RetrieveAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class AllClientView(generics.ListAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class NewClientRoomView(generics.CreateAPIView):
	queryset = ClientRoom.objects.all()
	serializer_class = NewClientRoomSerializer


class GetClientRoomView(generics.RetrieveAPIView):
	queryset = ClientRoom.objects.all()
	serializer_class = ClientRoomSerializer


class AllClientRoomView(generics.ListAPIView):
	serializer_class = ClientRoomSerializer

	def get_queryset(self):
		queryset = ClientRoom.objects.all()

		date1 = self.request.query_params.get('date1', None)
		date2 = self.request.query_params.get('date2', None)
		room_type = self.request.query_params.get('room_type', None)
		from_city = self.request.query_params.get('from_city', None)

		if date1:
			queryset = queryset.filter(arrival_date__gte=date1)

		if date2:
			queryset = queryset.filter(departure_date__lte=date2)

		if room_type:
			queryset = queryset.filter(room__room_type=room_type)

		if from_city:
			queryset = queryset.filter(client__city_from=from_city)

		return queryset


class NewCleaningView(generics.CreateAPIView):
	queryset = Cleaning.objects.all()
	serializer_class = NewCleaningSerializer


class GetCleaningView(generics.RetrieveAPIView):
	queryset = Cleaning.objects.all()
	serializer_class = CleaningSerializer


class AllCleaningView(generics.ListAPIView):
	serializer_class = CleaningSerializer

	def get_queryset(self):
		queryset = Cleaning.objects.all()

		servant = self.request.query_params.get('servant', None)

		if servant:
			queryset = queryset.filter(employee__user__username=servant)
		
		return queryset


class NewEmployeeView(generics.CreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


class GetEmployeeView(generics.RetrieveUpdateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


class AllEmployeeView(generics.ListAPIView):
	serializer_class = EmployeeSerializer

	def get_queryset(self):
		queryset = Employee.objects.all()

		username = self.request.query_params.get('username', None)

		employee_position = self.request.query_params.get('employee_position', None)

		if username:
			queryset = queryset.filter(user__username=username)

		if employee_position:
			queryset = queryset.filter(position=employee_position)

		return queryset
