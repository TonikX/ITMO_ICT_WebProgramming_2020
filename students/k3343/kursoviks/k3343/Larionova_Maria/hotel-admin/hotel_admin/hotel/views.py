from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *


class CreateFloorView(generics.CreateAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class RetrieveFloorView(generics.RetrieveAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class ListFloorView(generics.ListAPIView):
	queryset = Floor.objects.all()
	serializer_class = FloorSerializer


class CreateRoomView(generics.CreateAPIView):
	queryset = Room.objects.all()
	serializer_class = CreateRoomSerializer


class RetrieveRoomView(generics.RetrieveUpdateAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class ListRoomView(generics.ListAPIView):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class CreateClientView(generics.CreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class RetrieveClientView(generics.RetrieveAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class ListClientView(generics.ListAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer


class CreateClientRoomView(generics.CreateAPIView):
	queryset = ClientRoom.objects.all()
	serializer_class = CreateClientRoomSerializer


class RetrieveClientRoomView(generics.RetrieveAPIView):
	queryset = ClientRoom.objects.all()
	serializer_class = ClientRoomSerializer


class ListClientRoomView(generics.ListAPIView):
	queryset = ClientRoom.objects.all()
	serializer_class = ClientRoomSerializer


class CreateCleaningView(generics.CreateAPIView):
	queryset = Cleaning.objects.all()
	serializer_class = CleaningSerializer


class RetrieveCleaningView(generics.RetrieveAPIView):
	queryset = Cleaning.objects.all()
	serializer_class = CleaningSerializer


class ListCleaningView(generics.ListAPIView):
	serializer_class = CleaningSerializer

	def get_queryset(self):
		queryset = Cleaning.objects.all()

		worker = self.request.query_params.get('worker', None)

		if worker:
			queryset = queryset.filter(employee__user__username=worker)
		
		return queryset


class CreateChallengerView(generics.CreateAPIView):
	queryset = Challengers.objects.all()
	serializer_class = ChallengerSerializer


class CreateRequestView(generics.CreateAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer


class UpdateRequestView(generics.UpdateAPIView):
	queryset = Request.objects.all()
	serializer_class = RequestSerializer


class RetrieveReuqestView(generics.ListAPIView):
	serializer_class = GetRequestSerializer

	def get_queryset(self):
		queryset = Request.objects.all()

		username = self.request.query_params.get('username', None)

		if username:
			queryset = queryset.filter(challenger__user__username=username)

		return queryset
