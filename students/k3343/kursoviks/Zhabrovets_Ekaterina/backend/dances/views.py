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
from .custom_permissions import IsTeacher
from operator import itemgetter


class CreateWSH(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def post(self, request):
        serializer = WorkshopAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

class AskForPart(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        user = request.user
        wsh = request.data.get("wsh")
        workshop = Workshop.objects.get(id=wsh)
        QueryForParticipance.objects.create(user=user, workshop=workshop)
        return Response(status=201)

class UserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        user = request.user
        serializer = ParticipantsSerializer(user)
        return Response({"data": serializer.data})

class QueryPartInfo(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        user = request.user
        queries = QueryForParticipance.objects.filter(user=user).order_by('-workshop__date')
        serializer1 = QuerySerializer(queries, many=True)
        today = str(datetime.date.today())
        wsh = Workshop.objects.filter(date__lt=today, participants=user).order_by('-date')
        serializer2 = WorkshopSerializer(wsh, many=True)
        return Response({"data_fut": serializer1.data, 'data_prev':serializer2.data})

class WriteFeedback(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        user = request.user
        wsh = request.data.get("wsh")
        workshop = Workshop.objects.get(id=wsh)
        text = request.data.get("text")
        rating = request.data.get("rating")
        Feedback.objects.create(user=user, workshop=workshop, text=text, rating=rating)
        return Response(status=201)


class Wsh(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        today = str(datetime.date.today())
        wsh = Workshop.objects.filter(date__gte=today).order_by('date')
        serializer = WorkshopSerializer(wsh, many=True)
        return Response({"data": serializer.data})
#
#     def post(self, request):
#         wsh = request.data.get("wsh")
#         part = request.data.get("partic")
#         try:
#             workshop = Workshop.objects.get(id=wsh)
#             workshop.participants.add(part)
#             workshop.save()
#             return Response(status=201)
#         except:
#             return Response(status=400)
#
#
# class NotInclPeople(APIView):
#     permission_classes = [permissions.AllowAny, ]
#
#     def get(self, request):
#         workshop = request.GET.get("workshop")
#         w1 = Workshop.objects.get(id=workshop)
#         w1 = list(w1.participants.all())
#         w1 = [part.id for part in w1]
#         not_incl = Participant.objects.exclude(id__in=w1)
#         serializer = ParticipantsSerializer(not_incl, many=True)
#         return Response({"data": serializer.data})
#
#

class PartcipantsPerWSH(APIView):
    permission_classes = [permissions.IsAdminUser | IsTeacher]

    def get(self, request):
        wsh = request.GET.get('wsh')
        wsh = Workshop.objects.get(id=wsh)
        participants = wsh.participants.all()
        serializer = ParticipantsSerializer(participants, many=True)
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


class HallsForSchool(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        school = request.GET.get("school")
        halls = Hall.objects.filter(school=school)
        serializer = HallSerializer(halls, many=True)
        return Response({"data": serializer.data})

class AllSchools(APIView):
    permission_classes = [IsTeacher | permissions.IsAdminUser]

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
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request):
        style = request.GET.get("style")
        teachers = User.objects.filter(style=style)
        serializer = ChoreographersSerializer(teachers, many=True)
        return Response({"data": serializer.data})
#
#
class AddTeachersForWSH(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def post(self, request):
        workshop = Workshop.objects.all().order_by("-id")[0]
        teacher = request.data.get("teacher")
        try:
            workshop.choreographer.add(teacher)
            workshop.save()
            return Response(status=201)
        except:
            return Response(status=400)


class AllTeachers(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teachers = User.objects.filter(is_teacher=True)
        serializer = ParticipantsSerializer(teachers, many=True)
        return Response({"data": serializer.data})

class TeacherInfo(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teacher = request.GET.get("teacher")
        user = User.objects.get(id=teacher)
        serializer = ParticipantsSerializer(user)
        return Response({"data": serializer.data})

class FeedbackForTeacher(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teacher = request.GET.get("teacher")
        feedbacks = Feedback.objects.filter(workshop__choreographer=teacher).order_by('-created')
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response({"data": serializer.data})


# class AllQueryPartInfo(APIView):
#     permission_classes = [permissions.IsAuthenticated,]
#
#     def get(self, request):
#         queries = QueryForParticipance.objects.filter(approved=False)
#         serializer = QuerySerializer(queries, many=True)
#         return Response({"data": serializer.data})

class AllQueryPartInfo2(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        queries = QueryForParticipance.objects.filter(approved=False)
        serializer = QueriesAll(queries, many=True)
        count=queries.count()
        return Response({"data": serializer.data, "count":count})

class ApprovePartQueryAndAddPart(APIView):
    permission_classes = [permissions.IsAdminUser,]

    def post(self, request):
        q = request.data.get("id_query")
        try:
            query = QueryForParticipance.objects.get(id=q)
            query.approved = True
            query.save()
            workshop = Workshop.objects.get(id=query.workshop.id)
            workshop.participants.add(query.user.id)
            workshop.save()
            return Response(status=201)
        except:
            return Response(status=400)

#
class ProfitInfo(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        sch = Location.objects.all()
        today = str(datetime.date.today())
        data = []
        for s in sch:
            gained_profit = 0
            future_profit = 0
            # school = LocationSerializer(s)
            prev = Workshop.objects.filter(place__school=s, date__lt=today)
            fut = Workshop.objects.filter(place__school=s, date__gt=today)
            number_prev = len(prev)
            costs_prev = prev.values("place__cost")
            dur_prev = prev.values("duration")
            for i in range(len(costs_prev)):
                gained_profit += list(costs_prev[i].values())[0] * list(dur_prev[i].values())[0]
            costs_fut = fut.values("place__cost")
            dur_fut = fut.values("duration")
            for i in range(len(costs_fut)):
                future_profit += list(costs_fut[i].values())[0] * list(dur_fut[i].values())[0]
            info = {}
            info['id'] = s.id
            info['name'] = s.name
            info['gained_profit'] = gained_profit
            info['number_prev'] = number_prev
            info['fut_profit'] = future_profit
            info['number_fut'] = len(fut)
            data.append(info)
        return Response({"data": data})
#
#
# class ProfitInfo(APIView):
#     permission_classes = [permissions.IsAuthenticated, ]
#
#     def get(self, request):
#         sch = Location.objects.all()
#         today = str(datetime.date.today())
#         data = []
#         gained_profit = 0
#         future_profit = 0
#         for s in sch:
#             # school = LocationSerializer(s)
#             prev = Workshop.objects.filter(place__school=s, date__lt=today)
#             fut = Workshop.objects.filter(place__school=s, date__gt=today)
#             number_prev = len(prev)
#             number_fut = len(fut)
#             costs_prev = prev.values("place__cost")
#             dur_prev = prev.values("place__capacity")
#             costs_fut = fut.values("place__cost")
#             dur_fut = fut.values("place__capacity")
#
#             info = {}
#             info['id'] = s.id
#             info['name'] = s.name
#             info['gained_profit'] = costs_prev
#             info['number_prev'] = number_prev
#             info['number_fut'] = costs_fut
#             data.append(info)
#         return Response(data)
#
#
# class AllTeachers(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny, ]
#     serializer_class = ChoreographersSerializer
#     queryset = Choreographer.objects.all()
#
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response({"data":serializer.data})
#
#     # def get(self, request):
#     #     ch = Choreographer.objects.all()
#     #     serializer = ChoreographersSerializer(ch, many=True)
#     #     return Response({"data": serializer.data})
#
#
# class NearestWshForTeacher(APIView):
#     permission_classes = [permissions.AllowAny, ]
#
#     def get(self, request):
#         teacher = request.GET.get("choreographer")
#         today = str(datetime.date.today())
#         fut = Workshop.objects.filter(choreographer=teacher, date__gt=today).order_by('date')
#         nearest = WorkshopSerializer(fut[0])
#         return Response({"data": nearest.data})
#
# class FilteredWSH(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny, ]
#
#     queryset = Workshop.objects.all().order_by('date')
#     serializer_class = WorkshopSerializer
#     filter_backends = (DjangoFilterBackend,)
#     # filterset_fields = {'choreographer__style':['exact'], 'date':['gte', 'lte', 'exact', 'gt', 'lt']}
# #
# #     def get_queryset(self):
# #         queryset = Workshop.objects.all().order_by('date')
# #         style = self.request.query_params.get('style', None)
# #         if style is not None:
# #             queryset = queryset.filter(choreographer__style=style)
# #         return queryset
#
#
#     def get(self, request):
#         queryset =self.get_queryset()
#         style = self.request.query_params.get('style', 0)
#         if int(style) != 0:
#             print('Ьла-бла')
#             queryset = queryset.filter(choreographer__style=style)
#         serializer = self.serializer_class(queryset, many=True)
#         return Response({"data":serializer.data})
#
#
class FilteredWSH(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        # style = request.GET.get("style")
        today = str(datetime.date.today())
        date_start = request.GET.get("date_start")
        date_end = request.GET.get("date_end")
        workshops = Workshop.objects.filter(date__gte=today)
        if date_end is None:
            wsh = workshops.filter(date__gte=date_start)
        elif date_start is None:
            wsh = workshops.filter(date__lte=date_end)
        else:
            wsh = workshops.filter(date__range=[date_start, date_end])
        serializer = WorkshopSerializer(wsh, many=True)
        return Response({"data": serializer.data})
#

class UpdateProfile(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = (DjangoFilterBackend,)

    serializer_class = ParticipantUpdateSerializer
    queryset = User.objects.all()

class AddNameForNewProfile(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        try:
            full_name = request.data.get("full_name")
            queryset = User.objects.all().order_by("-id")[0]
            queryset.full_name = full_name
            queryset.save()
            return Response(status=201)
        except:
            return Response(status=400)
#
# class OnePart(APIView):
#     permission_classes = [permissions.AllowAny, ]
#
#     def get(self, request):
#         person = request.GET.get("person")
#         p = Participant.objects.get(id=person)
#         serializer = ParticipantsSerializer(p)
#         return Response({"data": serializer.data})
#
# class IsTeaher(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         user = request.user.is_stuff
#         return user

class RatingUsers(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        queries = User.objects.all()
        serializer = RatingSerializer(queries, many=True)
        data = serializer.data
        data.sort(key=lambda dictionary: dictionary['wsh_count'], reverse=True)
        return Response({"data": data})

class DanceStyleGen(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]

    filter_backends = (DjangoFilterBackend,)
    queryset = DanceStyle.objects.all()
    serializer_class = StyleSerializer