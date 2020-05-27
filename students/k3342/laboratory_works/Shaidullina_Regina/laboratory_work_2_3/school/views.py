#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from school.models import Subject, Room, Teacher, Pupil, Class, Assessment, Timetable
from school.serializers import SubjectSerializers, RoomSerializers, TeacherSerializers, PupilSerializers, ClassSerializers, \
                                AssessmentSerializers, TimetableSerializers


class Subjects(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializers(subjects, many=True)
        #return Response(serializer.data)
        return Response({'data' : serializer.data})


class Rooms(APIView):

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})
    """
    def post(self, request):
        subject = RoomSerializers(data=request.data)
        if subject.is_vaid():
            subject.save(number=request.number)
            return Response(status=201)
        else:
            return Response(status=400)
    """


class RoomsWithSubject(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        subject = request.GET.get('subject')
        rooms = Room.objects.filter(subject=subject)
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})


class Teachers(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response({'data': serializer.data})


class Pupils(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        pupils = Pupil.objects.all()
        serializer = PupilSerializers(pupils, many=True)
        return Response({'data': serializer.data})


class Classes(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializers(classes, many=True)
        return Response({'data': serializer.data})


class Assessments(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        asses = Assessment.objects.all()
        serializer = AssessmentSerializers(asses, many=True)
        return Response({'data': serializer.data})


class Timetables(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        tt = Timetable.objects.all()
        serializer = TimetableSerializers(tt, many=True)
        return Response({'data': serializer.data})
