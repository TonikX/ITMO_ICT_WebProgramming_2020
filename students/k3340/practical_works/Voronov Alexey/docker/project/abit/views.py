from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from abit import models
from abit import serializers

# Create your views here.

class Study_Programs(APIView):

    def get(self, request):
        programs = models.Study_Program.objects.all()
        serializer = serializers.Study_Program_Serialzer(programs, many=True)
        return Response({'values': serializer.data})


class Study_Places(APIView):

    def get(self, request):
        places = models.Study_Place.objects.all()
        serializer = serializers.Study_Place_Serialzer(places, many=True)
        return Response({'values': serializer.data})

class Abiturients(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        abiturients = models.Abiturient.objects.all()
        serializer = serializers.Abitutient_Serialzer(abiturients, many=True)
        return Response({'values': serializer.data})

    def post(self, request):
        abit = serializers.Abitutient_Serialzer(data=request.data)
        if abit.is_valid():
            abit.save()
            return Response({'status': 'succes'})
        else:
            return Response({'status': 'error'})