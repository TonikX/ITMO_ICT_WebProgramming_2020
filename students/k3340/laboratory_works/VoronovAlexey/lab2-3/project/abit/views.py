from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from abit import models
from abit import serializers


# Create your views here.

class Study_Programs(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        programs = models.Study_Program.objects.all()
        serializer = serializers.Study_Program_Serialzer(programs, many=True)
        return Response({'values': serializer.data})

    def post(self, request):
        program = serializers.Study_Program_Serialzer(data=request.data)
        if program.is_valid():
            program.save()
            return Response({'status': 'succes'})
        else:
            return Response({'status': 'error'})


class Study_Places(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        places = models.Study_Place.objects.all()
        serializer = serializers.Study_Place_Serialzer(places, many=True)
        return Response({'values': serializer.data})

    def post(self, request):
        place = serializers.Study_Place_Serialzer(data=request.data)
        if place.is_valid():
            place.save()
            return Response({'status': 'succes'})
        else:
            return Response({'status': 'error'})

class Abiturients(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        abiturients = models.Abiturient.objects.all()
        serializer = serializers.Abitutient_Serialzer_Get(abiturients, many=True)
        return Response({'values': serializer.data})

    def post(self, request):
        abit = serializers.Abitutient_Serialzer_Post(data=request.data)
        if abit.is_valid():
            abit.save()
            return Response({'status': 'succes'})
        else:
            print(abit.errors)
            return Response({'status': 'error'})

class AbiturientSetStatus(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        dict_status = {'true': True, 'false': False}
        abit = models.Abiturient.objects.get(id=id)
        abit.accepted = dict_status[request.data['status']]
        abit.save()
        print(abit.accepted)
        return Response({'status': 'succes'})

class AbiturientSetProgram(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        print(request.data['id_program'])
        abit = models.Abiturient.objects.get(id=id)
        abit.study_program = models.Study_Program.objects.get(id=request.data['id_program'])
        abit.save()
        print(abit.study_program)
        return Response({'status': 'succes'})


class Succeed_Abiturients(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        abiturients = models.Abiturient.objects.get(accepted=True)
        serializer = serializers.Abitutient_Serialzer(abiturients, many=True)
        return Response({'values': serializer.data})