from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions


class Part(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        ppl = Participant.objects.all()
        serializer = ParticipantsSerializer(ppl, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        serializer2 = ParticipantsSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(status=201)
        else:
            return Response(status=400)


class Wsh(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        wsh = Workshop.objects.all()
        serializer = WorkshopSerializer(wsh, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        wsh = request.data.get("wsh")
        part = request.data.get("partic")
        try:
            workshop = Workshop.objects.get(id=wsh)
            workshop.participants.add(part)
            workshop.save()
            return Response(status=201)
        except:
            return Response(status=400)


class NotInclPeople(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        workshop = request.GET.get("workshop")
        w1 = Workshop.objects.get(id=workshop)
        w1 = list(w1.participants.all())
        w1 = [part.id for part in w1]
        not_incl = Participant.objects.exclude(id__in=w1)
        serializer = ParticipantsSerializer(not_incl, many=True)
        return Response({"data": serializer.data})


class RemovePartic(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        wsh = request.data.get("wsh")
        part = request.data.get("partic")
        try:
            workshop = Workshop.objects.get(id=wsh)
            workshop.participants.remove(part)
            workshop.save()
            return Response(status=201)
        except:
            return Response(status=400)


class CreateWSH(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        serializer = WorkshopAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class HallsForSchool(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        school = request.GET.get("school")
        halls = Hall.objects.filter(school=school)
        serializer = HallSerializer(halls, many=True)
        return Response({"data": serializer.data})

class AllSchools(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        sch = Location.objects.all()
        serializer = LocationSerializer(sch, many=True)
        return Response({"data": serializer.data})