from rest_framework import generics, permissions, viewsets, renderers
from django_filters.rest_framework import DjangoFilterBackend
from .service import TimetableFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
from django.db.models import Count, Avg
from .models import Teacher,Timetable,Klass,Pupil,Cabinet,Subject, Grade
from .serializers import (TeacherSerializer, TeacherDetailSerializer, TeacherAddSerializer, PupilSerializer,
                          PupilDetailSerializer, GradeCreateSerializer, PupilAddSerializer, TimetableSerializer,
                          TimetableAddSerializer, KlassSerializer, SubjectSerializer, CabinetSerializer,
                          KlassDetailSerializer, KlassAddSerializer, GradeSerializer)


class TeacherViewSet(viewsets.ModelViewSet):
    """CRUD для модели Учитель"""
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherSerializer
        elif self.action == 'update':
            return TeacherSerializer
        elif self.action == 'create':
            return TeacherAddSerializer
        elif self.action !='list':
            return TeacherDetailSerializer


class PupilViewSet(viewsets.ModelViewSet):
    """CRUD для модели Ученик"""
    queryset = Pupil.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PupilSerializer
        elif self.action == 'update':
            return PupilSerializer
        elif self.action == 'create':
            return PupilAddSerializer
        elif self.action !='list':
            return PupilDetailSerializer


class GradeViewSet(viewsets.ModelViewSet):
    """CRUD для модели Оценка"""
    queryset = Grade.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return GradeCreateSerializer
        elif self.action != 'create':
            return GradeSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    """CRUD для модели Расписание"""
    queryset = Timetable.objects.all()
    filter_backends = (DjangoFilterBackend,
                       )
    filterset_class = TimetableFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TimetableSerializer
        elif self.action == 'retrieve':
            return TimetableSerializer
        elif self.action == 'update':
            return TimetableSerializer
        elif self.action == 'create':
            return TimetableAddSerializer


class KlassViewSet(viewsets.ModelViewSet):
    """CRUD для модели Класс"""
    queryset = Klass.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return KlassSerializer
        elif self.action == 'create':
            return KlassAddSerializer
        elif self.action !='list':
            return KlassDetailSerializer


class CabinetViewSet(viewsets.ModelViewSet):
    """Отображение для модели Кабинет"""
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """Отображение для модели Предмет"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


"""Запросы к курсовой работе"""

class Query1(APIView):
    """Какой предмет будет в заданном классе, в заданный день недели на заданном уроке?"""

    def get(self, request):
        klass = request.GET.get('klass')
        #klass = '1'
        day = request.GET.get('day')
        #day = 'Среда'
        lesson = request.GET.get('lesson')
        #lesson = '5-11:30-12:15'
        timetable = Timetable.objects.get(day=day, klass_name=klass, lesson=lesson)
        serializer = TimetableSerializer(timetable, many=False)
        return Response({'data': serializer.data})


class Query2(APIView):
    """Сколько учителей преподает каждую из дисциплин в школе?"""

    def get(self, request):
        teachers = Teacher.objects.all()
        subjects = dict(Counter([teacher.subject.subject for teacher in teachers]))
        return Response({'data': subjects})


class Query3(APIView):
    """Список учителей, преподающих те же предметы, что и учитель, ведущий информатику в заданном классе"""

    def get(self, request):
        klass = request.GET.get('klass')
        #klass = '1'
        #subject = '1'
        subject = request.GET.get('subject')
        timetable = Timetable.objects.get(klass_name=klass, subject_name=subject)
        serializer = TimetableSerializer(timetable, many=False)
        '''subjects = Teacher.objects.filter(id=teacher_name)
        subj = [s.subject.id for s in subjects]
        teachers = Teacher.objects.filter(subject=subj)
        teacher = set([t.teacher.last_name for t in teachers])'''
        return Response({'data': serializer.data})



class Query4(APIView):
    """Сколько мальчиков и девочек в каждом классе?"""

    def get(self, request):
        results = Pupil.objects.values('klass', 'gender').order_by('klass').annotate(Count('gender'))
        return Response({'data': results})


class Query5(APIView):
    """Сколько кабинетов в школе для базовых и профильных дисциплин?"""

    def get(self, request):
        base = Cabinet.objects.filter(profile='Для_базовых_дисциплин').count()
        for_profile = Cabinet.objects.filter(profile='Для_профильных_дисциплин').count()
        results = {'Кабинеты для профильных дисциплин': for_profile, 'Кабинеты для базовых дисциплин': base}
        return Response({'data': results})


class KlassReport(APIView):
    """Получение отчета по классу"""

    def get(self, request):

        klass = request.GET.get('klass')
        #klass = '3'
        teacher = Klass.objects.get(id=klass).teacher.last_name
        pupils = Pupil.objects.filter(klass=klass)
        pupils_cnt = pupils.count()
        results = {
                'Количество учеников в классе': pupils_cnt,
                'Классный руководитель': teacher
            }
        return Response({'data': results})

