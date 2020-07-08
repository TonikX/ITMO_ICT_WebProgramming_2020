from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

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
        wsh = Workshop.objects.all().order_by('date')
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


class AllStyles(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        styles = DanceStyle.objects.all()
        serializer = StyleSerializer(styles, many=True)
        return Response({"data": serializer.data})


class TeachersForStyle(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        style = request.GET.get("style")
        teachers = Choreographer.objects.filter(style=style)
        serializer = ChoreographersSerializer(teachers, many=True)
        return Response({"data": serializer.data})


class AddTeachersForWSH(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        workshop = Workshop.objects.all().order_by("-id")[0]
        teacher = request.data.get("teacher")
        try:
            workshop.choreographer.add(teacher)
            workshop.save()
            return Response(status=201)
        except:
            return Response(status=400)


class ProfitInfo(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        sch = Location.objects.all()
        today = str(datetime.date.today())
        data = []
        gained_profit = 0
        future_profit = 0
        for s in sch:
            # school = LocationSerializer(s)
            prev = Workshop.objects.filter(place__school=s, date__lt=today)
            fut = Workshop.objects.filter(place__school=s, date__gt=today)
            number_prev = len(prev)
            costs_prev = prev.values("place__cost")
            for cost in costs_prev:
                gained_profit += list(cost.values())[0]
            costs_fut = fut.values("place__cost")
            for cost in costs_fut:
                future_profit += list(cost.values())[0]
            info = {}
            info['id'] = s.id
            info['name'] = s.name
            info['gained_profit'] = gained_profit
            info['number_prev'] = number_prev
            info['fut_profit'] = future_profit
            info['number_fut'] = len(fut)
            data.append(info)
        return Response({"data": data})



class AllTeachers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ChoreographersSerializer
    queryset = Choreographer.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({"data":serializer.data})


class NearestWshForTeacher(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        teacher = request.GET.get("choreographer")
        today = str(datetime.date.today())
        fut = Workshop.objects.filter(choreographer=teacher, date__gt=today).order_by('date')
        nearest = WorkshopSerializer(fut[0])
        return Response({"data": nearest.data})


class FilteredWSH(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        # style = request.GET.get("style")
        date_start = request.GET.get("date_start")
        date_end = request.GET.get("date_end")
        if date_end is None:
            wsh = Workshop.objects.filter(date__gte=date_start)
        elif date_start is None:
            wsh = Workshop.objects.filter(date__lte=date_end)
        else:
            wsh = Workshop.objects.filter(date__range=[date_start, date_end])
        serializer = WorkshopSerializer(wsh, many=True)
        return Response({"data": serializer.data})


class UpdateWSH(ModelViewSet):
    permission_classes = [permissions.AllowAny, ]

    serializer_class = ParticipantsSerializer
    queryset = Participant.objects.all()

class OnePart(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        person = request.GET.get("person")
        p = Participant.objects.get(id=person)
        serializer = ParticipantsSerializer(p)
        return Response({"data": serializer.data})