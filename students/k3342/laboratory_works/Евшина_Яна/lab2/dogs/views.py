from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Dog, Club, Show, Registration, Ring, \
    Perform, Grade
from .serializers import DogListSerializer, ClubListSerializer, \
    UserListSerializer, ShowListSerializer, RegistrationListSerializer, \
    RingListSerializer, PerformListSerializer, GradeListSerializer, \
    RegistrationSerializer


User = get_user_model()


class RegistrationAPI(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)


class DogListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer

    def get(self, request):
        dogs = self.queryset.filter(owner=request.user)
        serializer = self.serializer_class(dogs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DogDetailView(generics.RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer


class ClubListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubListSerializer
 #   permission_classes = (IsAuthenticated,)


class ExpertListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = User.objects.filter(expert=True)
    serializer_class = UserListSerializer


class UserDetailedView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        shows = self.queryset.all()
        allowed_dogs_by_show = {}

        print(shows)

        for show in shows:
            query = Dog.objects.filter(
                owner=request.user,
                registration__show__id=show.id,
                registration__fee=True
            )

            if len(query.values()):
                allowed_dogs_by_show[show.id] = list(map(lambda obj: obj['id'], query.values('id')))

        print(allowed_dogs_by_show)

        serializer = self.serializer_class(shows, many=True, allowed_dogs_by_show=allowed_dogs_by_show)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationListSerializer


class RingListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = RingListSerializer

    def get_queryset(self):
        show_id = self.kwargs['pk']
        queryset = Ring.objects.filter(show__id=show_id)

        return queryset


class PerformListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Perform.objects.all()
    serializer_class = PerformListSerializer


class GradeListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = GradeListSerializer

    def get_queryset(self):
        show_id = self.kwargs['pk']
        ring_id = self.kwargs['ring_id']
        queryset = Grade.objects.filter(
            perform__ring_id=ring_id,
            perform__ring__show_id=show_id,
        )

        return queryset


