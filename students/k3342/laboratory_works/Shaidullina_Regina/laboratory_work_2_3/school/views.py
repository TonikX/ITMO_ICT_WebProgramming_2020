#from django.shortcuts import render
from collections import Counter
from django.db.models import Count, Avg
from django.http import QueryDict, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from school.models import Subject, Room, Teacher, Pupil, Class, Assessment, Timetable, Teaching
from school.serializers import SubjectSerializers, RoomSerializers, TeacherSerializers, PupilSerializers, \
                                ClassSerializers, AssessmentSerializers, TimetableSerializers, TeachingSerializer


class Subjects(APIView):

    permission_classes = [permissions.IsAuthenticated, ]
    #permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializers(subjects, many=True)
        return Response({'data': serializer.data})


class Rooms(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})

    def put(self, request):
        tname = request.POST.get('teacher')
        rnum = request.POST.get('number')
        teacher = Teacher.objects.get(name=tname)
        actual_room = Room.objects.get(number=rnum)
        if Room.objects.filter(teacher=teacher):
            prev_rnum = request.POST.get('old_room')
            previous_room = Room.objects.get(number=prev_rnum)
            updated_room = Room(number=prev_rnum, floor=previous_room.floor, subject=previous_room.subject, teacher=None)
            updated_room.save()
        updated_room = Room(number=rnum, floor=actual_room.floor, subject=actual_room.subject, teacher=teacher)
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

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def delete(self, request):
        params = QueryDict(request.body)
        teacher = self.get_object(params['name'])
        teacher.delete()
        return Response(status=204)

    def put(self, request):
        params = QueryDict(request.body)
        teacher = self.get_object(params['name'])
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
        pupil = PupilSerializers(data=request.data)
        if pupil.is_valid():
            pupil.save()
            return Response({'data': pupil.data}, status=201)
        else:
            return Response(status=400)

    def get_object(self, pk):
        try:
            return Pupil.objects.get(pk=pk)
        except Pupil.DoesNotExist:
            raise Http404

    def delete(self, request):
        params = QueryDict(request.body)
        pupil = self.get_object(params['name'])
        pupil.delete()
        return Response(status=204)

    def put(self, request):
        params = QueryDict(request.body)
        pupil = self.get_object(params['name'])
        serializer = PupilSerializers(pupil, data=request.data)
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

    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404

    def put(self, request):
        tname = request.POST.get('guiding_teacher')
        clas = request.POST.get('name')
        teacher = Teacher.objects.get(name=tname)
        actual_class = Class.objects.get(name=clas)
        if Class.objects.filter(guiding_teacher=teacher):
            prev_clas = request.POST.get('old_class')
            # previous_class = Class.objects.get(name=prev_clas)
            updated_class = Class(name=prev_clas, guiding_teacher=None)
            updated_class.save()
        updated_class = Class(name=actual_class, guiding_teacher=teacher)
        updated_class.save()
        return Response(status=201)


class Assessments(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        asses = Assessment.objects.all()
        serializer = AssessmentSerializers(asses, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        a = AssessmentSerializers(data=request.data)
        if a.is_valid():
            a.save()
            return Response({'data': a.data}, status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        params = QueryDict(request.body)
        asse = Assessment.objects.filter(term=params['term'], pupil=params['pupil'], subject=params['subject'])
        asse.delete()
        return Response(status=204)

    def put(self, request):
        t = request.POST.get('term')
        p = Pupil.objects.get(name=request.POST.get('pupil'))
        s = Subject.objects.get(name=request.POST.get('subject'))
        g = request.POST.get('grade')
        old_g = request.POST.get('old_grade')
        grade = Assessment.objects.get(term=t, pupil=p, subject=s, grade=old_g)
        grade.delete()
        grade = Assessment(term=t, pupil=p, subject=s, grade=g)
        grade.save()
        return Response(status=201)


class AssessmentOne(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        t = request.GET.get('term')
        p = request.GET.get('pupil')
        s = request.GET.get('subject')
        grade = Assessment.objects.get(term=t, pupil=p, subject=s)
        serializer = AssessmentSerializers(grade)
        return Response({'data': serializer.data})


class Timetables(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        tt = Timetable.objects.all()
        serializer = TimetableSerializers(tt, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        a = TimetableSerializers(data=request.data)
        if a.is_valid():
            a.save()
            return Response({'data': a.data}, status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        params = QueryDict(request.body)
        t = Timetable.objects.filter(
            day_of_week=params['day_of_week'], 
            study_class=params['study_class'], 
            lesson_num=params['lesson_num'], 
            subject=params['subject'], 
            room=params['room'], 
            teacher=params['teacher']
        )
        t.delete()
        return Response(status=204)

    # def put(self, request):
    #     d = request.POST.get('day_of_week')
    #     c = Class.objects.get(name=request.POST.get('study_class'))
    #     ln = request.POST.get('lesson_num')
    #     s = Subject.objects.get(name=request.POST.get('subject'))
    #     r = Room.objects.get(name=request.POST.get('room'))
    #     t = Teacher.objects.get(name=request.POST.get('teacher'))
    #     # old_g = request.POST.get('old_grade')
    #     # grade = Assessment.objects.get(term=t, pupil=p, subject=s, grade=old_g)
    #     # grade.delete()
    #     # grade = Assessment(term=t, pupil=p, subject=s, grade=g)
    #     # grade.save()
    #     # return Response(status=201)


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


class Query1(APIView):
    """ Какой предмет будет в заданном классе в заданный день недели на заданном уроке? """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        c = request.GET.get('study_class')
        d = request.GET.get('day_of_week')
        l = request.GET.get('lesson_num')
        tt = Timetable.objects.get(day_of_week=d, study_class=c, lesson_num=l)
        serializer = TimetableSerializers(tt, many=False)
        return Response({'data': serializer.data})


class Query2(APIView):
    """ Сколько учителей преподает каждую из дисциплин в школе? """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        tg = Teaching.objects.all()
        subs = dict(Counter([t.subject.name for t in tg]))
        return Response({'data': subs})


class Query3(APIView):
    """ Список учителей, преподающих те же предметы, что и учитель, ведущий информатику в заданном классе. """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        # Note: for one teacher only
        c = request.GET.get('study_class')
        s = 'informatics'
        tt = Timetable.objects.filter(study_class=c, subject=s)
        tname = tt[0].teacher
        subjects = Teaching.objects.filter(teacher=tname)
        subs = [s.subject.name for s in subjects]
        tts = Teaching.objects.filter(subject__in=subs)
        teachers = set([t.teacher.name for t in tts])
        return Response({'data': teachers})


class Query4(APIView):
    """ Сколько мальчиков и девочек в каждом классе? """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        results = Pupil.objects.values('study_class', 'gender').order_by('study_class').annotate(Count('gender'))
        return Response({'data': results})


class Query5(APIView):
    """ Сколько кабинетов в школе для базовых и профильных дисциплин? """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        r = Room.objects.all()
        minors = Subject.objects.filter(sub_type='minor')
        majors = Subject.objects.filter(sub_type='major')
        minors, majors = [m.name for m in minors], [m.name for m in majors]
        rooms_minor = Room.objects.filter(subject__in=minors).count()
        rooms_major = Room.objects.filter(subject__in=majors).count()
        results = {'Minor subjects': rooms_minor, 'Major subjects': rooms_major}
        return Response({'data': results})


class Report(APIView):
    """
    Отчет об успеваемости заданного класса.
    Отчет включает сведения об успеваемости за четверть по каждому предмету.
    Необходимо подсчитать средний балл по каждому предмету, по классу в целом, указать общее количество учеников в классе.
    Для класса указать классного руководителя.
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        c = request.GET.get('class')
        guiding_teacher = Class.objects.get(name=c).guiding_teacher.name
        pupils = Pupil.objects.filter(study_class=c)
        pupils_cnt = pupils.count()
        pupils = [p.name for p in pupils]
        grades = Assessment.objects.filter(pupil__in=pupils)
        avg_grade = round(grades.aggregate(Avg('grade'))['grade__avg'],2)
        avg_sub_grades = grades.values('subject').annotate(Avg('grade'))
        results = {
            'Average grade per each subject': avg_sub_grades,
            'results': {
                'Average grade in class': avg_grade,
                'Total pupls in class' : pupils_cnt,
                'Guiding teacher': guiding_teacher
            }
        }
        return Response({'data': AssessmentSerializers(grades, many=True).data, 'results': results})
