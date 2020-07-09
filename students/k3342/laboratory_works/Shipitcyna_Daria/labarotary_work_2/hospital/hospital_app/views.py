from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from rest_framework.parsers import JSONParser
import datetime
import json
from .models import Patient, Appointment, Schedule, Doctor
from .serializers import *


class Patients(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        patients = PatientPostSerializer(data=request.data)
        print(patients)
        if patients.is_valid():
            patients.save()
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class PatientDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Patient.objects.all()
    print(Patient.objects.all())
    serializer_class = PatientSerializer


class AppointmentDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class PatientUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Patient.objects.all()
    serializer_class = PatientPostSerializer


class PatientDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Patient.objects.all()
    serializer_class = PatientPostSerializer


class DocFreeTime(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        doctor = request.GET.get("doctor", None)
        doctor_object = Doctor.objects.filter(id=doctor)[0]
        print(doctor_object)
        if doctor:
            busy = Appointment.objects.filter(record__doctor=doctor).values_list('record__app_time')
            # schedule_objects = Schedule.objects.filter(doctor=doctor, app_time=busy)
            # record = schedule_objects.app_time.exclude(id__in=busy)
            # print(schedule_objects)
            free = doctor_object.work_times.exclude(id__in=busy)
        else:
            free = []
        serializer = TimesSerializer(free, many=True)
        return Response({"data": serializer.data})


class Doctors(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        docs = Doctor.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        docs = DoctorPostSerializer(data=request.data)
        print(docs)
        if docs.is_valid():
            print('it is valid')
            docs.save()
            return Response({"status": "Add"})
        else:
            print('its not valid')
            return Response({"status": "Error"})


class Appointments(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = AppointmentFilterSerializer
    queryset = Appointment.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    # parser_classes = [JSONParser]
    # search_fields = ('patient__id', 'record__doctor__type')
    filter_fields = ('record__doctor__surname', 'patient__surname', 'record__doctor__type', 'record__app_time__date')


class Apps(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        apps = Appointment.objects.all()
        serializer = AppointmentSerializer(apps, many=True)
        return Response({"data": serializer.data})


class AppDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        patient = request.GET.get("patient_id", None)
        schedule = request.GET.get("schedule_id", None)
        apps = Appointment.objects.filter(patient=patient_id, schedule=schedule_id)
        serializer = AppointmentSerializer(apps, many=True)
        return Response({"data": serializer.data})


class AppTimesList(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        times = App_times.objects.all()
        serializer = TimesSerializer(times, many=True)
        return Response({"data": serializer.data})


class Services(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        services = PriceList.objects.all()
        serializer = PriceSerializer(services, many=True)
        print(serializer.data)
        return Response({"data": serializer.data})


class CreateApp(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentPostSerializer
    parser_classes = [JSONParser]

    def create(self, request, *args, **kwargs):
        app = self.serializer_class(data=request.data)
        print(app)
        if app.is_valid():
            app.save()
            return Response({'status': 'added'})
        else:
            return Response({'status': 'error'})


class AppUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentPostSerializer
    parser_classes = [JSONParser]

    def create(self, request, *args, **kwargs):
        app = self.serializer_class(data=request.data)
        print(app)
        if app.is_valid():
            app.save()
            return Response({'status': 'added'})
        else:
            return Response({'status': 'error'})


class CreateDoctor(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Doctor.objects.all()
    serializer_class = DoctorPostSerializer
    # parser_classes = [JSONParser]

    def create(self, request, *args, **kwargs):
        doc = self.serializer_class(data=request.data)
        print(doc)
        if doc.is_valid():
            doc.save()
            return Response({'status': 'added'})
        else:
            return Response({'status': 'error'})


class MedCard(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        patient_id = request.GET.get("id", None)
        if id:
            patient = Patient.objects.get(id=patient_id)
            apps = Appointment.objects.filter(patient=patient)
        else:
            apps = []
        serializer = MedCardSerializer(apps, many=True)

        return Response({"data": serializer.data})


class ScheduleView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        doctor_id = request.GET.get("id", None)
        if doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            schedules = Schedule.objects.filter(doctor=doctor)
            actual_schedules = []
            today = datetime.date.today()
            for i in range(len(schedules)):
                if schedules[i].app_time.date >= today:
                    actual_schedules.append(schedules[i])
        else:
            actual_schedules = []
        serializer = ScheduleSerializer(actual_schedules, many=True)

        return Response({"data": serializer.data})


class QuerySet1(APIView):
    """Количество приемов у каждого врача"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        app_num = Appointment.objects.values('record__doctor__surname').annotate(amount=Count("id")).order_by('-amount')
        # serializer = QuerySet1Serializer(app_num)
        return Response({"data": app_num})


class QuerySet2(APIView):
    """Количество врчей каждой специализации"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        type_num = Doctor.objects.values('type').annotate(amount=Count("type"))
        return Response({"data": type_num})


class QuerySet3(APIView):
    """Стоимость всех приемов у каждого врача"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self,request):
        sum = Appointment.objects.values('record__doctor__surname').annotate(amount=Sum("service__price")).order_by('-amount')
        return Response({"data": sum})


class QuerySet4(APIView):
    """Количество приемов у врача по дате """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        date = request.GET.get('date')
        doctor = request.GET.get('doctor')
        apps = Appointment.objects.filter(record__doctor__surname=doctor, record__app_time__date=date)
        app_num = apps.values('record__app_time__date', 'record__doctor__surname').annotate(amount=Count("id"))
        return Response({"data": app_num})


class Report(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
        apps = Appointment.objects.filter(record__app_time__date__gte=date_start, record__app_time__date__lte=date_end)
        app_sum = apps.values('id').annotate(amount=Sum("service__price"))
        return Response({"data": app_sum})

