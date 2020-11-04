from rest_framework import generics, permissions

from .serializers import *
from .models import *


class HumanListView(generics.ListAPIView):
    serializer_class = HumanSerializer

    def get_queryset(self):
        queryset = Human.objects.all()

        params = self.request.query_params

        org = params.get('org', None)
        user = params.get('user', None)

        if org:
            queryset = queryset.filter(org=org)

        if user:
            queryset = queryset.filter(user__username=user)

        return queryset


class CreateHumanView(generics.CreateAPIView):
    queryset = Human.objects.all()
    serializer_class = NewHumanSerializer


class GetHumanView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = NewHumanSerializer


class IfClientView(generics.ListAPIView):
    serializer_class = HumanSerializer

    def get_queryset(self):
        queryset = Human.objects.all()

        params = self.request.query_params

        user = params.get('user', None)

        if user:
            queryset = queryset.filter(user__username=user)
            return queryset


class DogsListView(generics.ListAPIView):
    serializer_class = DogsSerializer

    def get_queryset(self):
        queryset = Dogs.objects.all()

        params = self.request.query_params

        dog_club = params.get('dog_club', None)
        dog_breed = params.get('dog_breed', None)
        dog_owner = params.get('dog_owner', None)

        if dog_club:
            queryset = queryset.filter(dog_club=dog_club)

        if dog_breed:
            queryset = queryset.filter(dog_breed=dog_breed)

        if dog_owner:
            queryset = queryset.filter(dog_owner__id=dog_owner)

        return queryset


class CreateDogView(generics.CreateAPIView):
    queryset = Dogs.objects.all()
    serializer_class = NewDogsSerializer


class GetDogView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dogs.objects.all()
    serializer_class = DogsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ExpertsListView(generics.ListAPIView):
    queryset = Experts.objects.all()
    serializer_class = ExpertsSerializer


class CreateExpertView(generics.CreateAPIView):
    queryset = Experts.objects.all()
    serializer_class = ExpertsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetExpertView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experts.objects.all()
    serializer_class = ExpertsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class FundersListView(generics.ListAPIView):
    queryset = Funders.objects.all()
    serializer_class = FundersSerializer


class CreateFunderView(generics.CreateAPIView):
    queryset = Funders.objects.all()
    serializer_class = FundersSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetFunderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funders.objects.all()
    serializer_class = FundersSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class RingsListView(generics.ListAPIView):
    queryset = Rings.objects.all()
    serializer_class = RingsSerializer


class CreateRingView(generics.CreateAPIView):
    queryset = Rings.objects.all()
    serializer_class = RingsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetRingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rings.objects.all()
    serializer_class = RingsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ShowsListView(generics.ListAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer


class CreateShowView(generics.CreateAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetShowView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class RecordsListView(generics.ListAPIView):
    serializer_class = RecordsSerializer

    def get_queryset(self):
        queryset = Records.objects.all()

        params = self.request.query_params

        record_confirmation = params.get('record_confirmation', None)
        record_show = params.get('record_show', None)

        if record_confirmation:
            queryset = queryset.filter(record_confirmation=record_confirmation)

        if record_show:
            queryset = queryset.filter(record_show__id=record_show)

        return queryset


class CreateRecordView(generics.CreateAPIView):
    queryset = Records.objects.all()
    serializer_class = NewRecordsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetRecordView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ActsListView(generics.ListAPIView):
    serializer_class = ActsSerializer

    def get_queryset(self):
        queryset = Acts.objects.all()

        params = self.request.query_params

        act_dog = params.get('act_dog', None)

        if act_dog:
            queryset = queryset.filter(act_dog__id=act_dog)

        return queryset


class CreateActView(generics.CreateAPIView):
    queryset = Acts.objects.all()
    serializer_class = NewActsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetActView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acts.objects.all()
    serializer_class = ActsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class SponsorsListView(generics.ListAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer


class CreateSponsorView(generics.CreateAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = NewSponsorsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetSponsorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class JudgingsListView(generics.ListAPIView):
    serializer_class = JudgingsSerializer

    def get_queryset(self):
        queryset = Judgings.objects.all()

        params = self.request.query_params

        judging_ring = params.get('judging_ring', None)

        if judging_ring:
            queryset = queryset.filter(judging_ring__id=judging_ring)

        return queryset


class CreateJudgingView(generics.CreateAPIView):
    queryset = Judgings.objects.all()
    serializer_class = NewJudgingsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class GetJudgingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Judgings.objects.all()
    serializer_class = JudgingsSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly
