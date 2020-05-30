#from django.shortcuts import render
from django.http import QueryDict, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from school.models import Subject, Room, Teacher, Pupil, Class, Assessment, Timetable, Teaching
from school.serializers import SubjectSerializers, RoomSerializers, TeacherSerializers, PupilSerializers, PupilPostSerializers, \
                                ClassSerializers, AssessmentSerializers, TimetableSerializers, TeachingSerializer


class Subjects(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializers(subjects, many=True)
        #return Response(serializer.data)
        return Response({'data': serializer.data})


class Rooms(APIView):

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})

    def get_edited_object(self, pk):
        try:
            return Room.objects.get(number=pk)
        except Room.DoesNotExist:
            raise Http404

    def put(self, request):
        params = QueryDict(request.body)
        teacher = Teacher.objects.get(name=params['teacher'])
        room = self.get_edited_object(params['number'])
        actual_room = Room.objects.get(number=params['number'])
        updated_room = Room(number=room, floor=actual_room.floor, subject=actual_room.subject, teacher=teacher)
        updated_room.save()
        return Response(status=201)


# class RoomsWithSubject(APIView):

#     permission_classes = [permissions.IsAuthenticated, ]

#     def get(self, request):
#         subject = request.GET.get('subject')
#         rooms = Room.objects.filter(subject=subject)
#         serializer = RoomSerializers(rooms, many=True)
#         return Response({'data': serializer.data})


class Teachers(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        teacher = TeacherSerializers(data=request.data)
        if teacher.is_valid():
            teacher.save()
            return Response({'data': teacher.data}, status=201)
        else:
            return Response(status=400)

    def get_object(self, parameter):
        try:
            return Teacher.objects.get(name=parameter)
        except Teacher.DoesNotExist:
            raise Http404

    def delete(self, request):
        params = QueryDict(request.body)
        teacher = self.get_object(params['name'])
        teacher.delete()
        return Response(status=204)

    def get_edited_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def put(self, request):
        params = QueryDict(request.body)
        teacher = self.get_edited_object(params['id'])
        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=201)
        else:
            return Response(status=400)


class TeacherOne(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        teacher_name = request.GET.get('name')
        teacher = Teacher.objects.get(name=teacher_name)
        serializer = TeacherSerializers(teacher)
        return Response({'data': serializer.data})


class Pupils(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        pupils = Pupil.objects.all()
        serializer = PupilSerializers(pupils, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        pupil = PupilPostSerializers(data=request.data)
        if pupil.is_valid():
            pupil.save()
            return Response({'data': pupil.data}, status=201)
        else:
            return Response(status=400)

    def get_object(self, parameter):
        try:
            return Pupil.objects.get(name=parameter)
        except Pupil.DoesNotExist:
            raise Http404

    def delete(self, request):
        params = QueryDict(request.body)
        pupil = self.get_object(params['name'])
        pupil.delete()
        return Response(status=204)

    def get_edited_object(self, pk):
        try:
            return Pupil.objects.get(pk=pk)
        except Pupil.DoesNotExist:
            raise Http404

    def put(self, request):
        params = QueryDict(request.body)
        pupil = self.get_edited_object(params['id'])
        serializer = PupilPostSerializers(pupil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=201)
        else:
            return Response(status=400)


class PupilOne(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        pupil_name = request.GET.get('name')
        pupil = Pupil.objects.get(name=pupil_name)
        serializer = PupilSerializers(pupil)
        return Response({'data': serializer.data})


class Classes(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializers(classes, many=True)
        return Response({'data': serializer.data})

    def get_edited_object(self, pk):
        try:
            return Class.objects.get(name=pk)
        except Class.DoesNotExist:
            raise Http404

    def put(self, request):
        params = QueryDict(request.body)
        teacher = Teacher.objects.get(name=params['guiding_teacher'])
        clas = self.get_edited_object(params['name'])
        updated_class = Class(name=clas, guiding_teacher=teacher)
        updated_class.save()
        return Response(status=201)


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


class Teachings(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        t = Teaching.objects.all()
        serializer = TeachingSerializer(t, many=True)
        return Response({'data': serializer.data})

    def put(self, request):
        tname = request.POST.get('teacher')
        subjects = request.POST.getlist('subject[]')
        teacher = Teacher.objects.get(name=tname)
        for s in subjects:
            s_instance = Subject.objects.get(name=s)
            new_t = Teaching(teacher=teacher, subject=s_instance)
            new_t.save()
        return Response(status=201)
