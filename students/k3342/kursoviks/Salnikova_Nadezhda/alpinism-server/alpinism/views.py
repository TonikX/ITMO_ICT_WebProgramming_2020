from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, status
from django.http import QueryDict, Http404
from django_filters.rest_framework import DjangoFilterBackend

from alpinism.models import *
from alpinism.serializers import *
from alpinism.filters import *


class CountryView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        country = CountrySerializer(data=request.data)
        if country.is_valid():
            country.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClubView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        club = ClubPostSerializer(data=request.data)
        if club.is_valid():
            club.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Club.objects.get(pk=pk)
        except Club.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MountainView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        mountains = Mountain.objects.all()
        serializer = MountainSerializer(mountains, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        mountain = MountainPostSerializer(data=request.data)
        if mountain.is_valid():
            mountain.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Mountain.objects.get(pk=pk)
        except Mountain.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        mountain = self.get_one(put_params['id'])
        serializer = GroupPostSerializer(mountain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlpinistView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        alpinists = Alpinist.objects.all()
        serializer = AlpinistSerializer(alpinists, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        alpinist = AlpinistPostSerializer(data=request.data)
        if alpinist.is_valid():
            alpinist.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Alpinist.objects.get(pk=pk)
        except Alpinist.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        # group = request.GET.get("group")
        # group = 1
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response({"data": serializer.data})

    def post(self, request, format=None):
        serializer = GroupPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_one(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        put_params = QueryDict(request.body)
        group = self.get_one(put_params['id'])
        serializer = GroupPostSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndSuccessView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        successes = IndSuccess.objects.all()
        serializer = IndSuccessSerializer(successes, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        ind_success = IndSuccessPostSerializer(data=request.data)
        if ind_success.is_valid():
            ind_success.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return IndSuccess.objects.get(pk=pk)
        except IndSuccess.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AscentView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        ascents = Ascent.objects.all()
        serializer = AscentSerializer(ascents, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        ascent = AscentPostSerializer(data=request.data)
        if ascent.is_valid():
            ascent.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Ascent.objects.get(pk=pk)
        except Ascent.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmergencyView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        emergencies = Emergency.objects.all()
        serializer = EmergencySerializer(emergencies, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        emergency = EmergencyPostSerializer(data=request.data)
        if emergency.is_valid():
            emergency.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def get_one(self, pk):
        try:
            return Emergency.objects.get(pk=pk)
        except Emergency.DoesNotExist:
            raise Http404

    def delete(self, request):
        delete_params = QueryDict(request.body)
        obj = self.get_one(delete_params['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Request1View(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, format=None):
        mountain_name = request.GET.get("mountain_name")
        mountain = Mountain.objects.get(mountain_name=mountain_name)
        ascents = Ascent.objects.filter(mountain=mountain)
        serializer = AscentSerializer(ascents, many=True)
        if ascents:
            return Response(serializer.data)
        return Http404


class Request2View(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        params = request.GET.get("start_date", "end_date")
        start_date = params[0]
        end_date = params[1]
        emergencies = Emergency.objects.get(date > start_date)
        serializer = EmergencySerializer(emergencies, many=True)
        if emergencies:
            return Response(serializer.data)
        return Http404
