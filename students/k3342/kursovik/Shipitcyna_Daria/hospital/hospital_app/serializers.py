from abc import ABC

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import datetime


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'surname', 'name', 'patronymic', 'birth_date', 'sex', 'phone', 'email')


class PatientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('surname', 'name', 'patronymic', 'birth_date', 'sex', 'phone', 'email')


class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = App_times
        fields = ('id', 'date', 'time_start')


class DoctorSerializer(serializers.ModelSerializer):
    # work_times = ScheduleSerializer()

    class Meta:
        model = Doctor
        fields = ('id', 'surname', 'name', 'patronymic', 'education', 'category', 'type', 'sex', 'phone', 'email', 'work_times')


class DoctorPostSerializer(serializers.ModelSerializer):
    work_times = serializers.PrimaryKeyRelatedField(queryset=App_times.objects.all())
    # work_times = serializers.PrimaryKeyRelatedField(queryset=App_times.objects.all(), write_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ('surname', 'name', 'patronymic', 'education', 'category', 'type', 'sex', 'phone', 'email',
                  'work_times')

    # переопределяем метод create сериализатора, чтобы при помощи полученных данных - получить необходимый
    # объект Schedule (с доктором и датой-временем посещения), а так же добавить услуги к создаваемому приему
    def create(self, validated_data):
        # work_times = App_times.objects.get(id=validated_data['work_times'])

        doc = Doctor.objects.create()

        for time in validated_data['work_times']:
            doc.work_times.add(time)

        return doc


class ScheduleSerializer(serializers.ModelSerializer):
    app_time = TimesSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Schedule
        fields = ('id', 'app_time', 'doctor')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ('id', 'service', 'price')


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    record = ScheduleSerializer()
    service = PriceSerializer(many=True)

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'record', 'service', 'paid', 'diagnosis')


class AppointmentFilterSerializer(serializers.ModelSerializer):
    # patient = serializers.SlugRelatedField(slug_field="surname", read_only=True)
    # record = serializers.SlugRelatedField(slug_field="id", read_only=True)
    # service = PriceSerializer()

    class Meta:
        model = Appointment
        fields = ('patient', 'record', 'paid')


class AppointmentPostSerializer(serializers.ModelSerializer):
    # каждый необходимый нам объект определяем полем PrimaryKeyRelatedField - чтобы сериализатор знал, с
    # какими объектами мы работаем и брал их по id, т.к. в запросе с клиента нам приходят id объектов
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    date = serializers.PrimaryKeyRelatedField(queryset=App_times.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=PriceList.objects.all(), many=True)

    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'date', 'service', 'diagnosis')

    # переопределяем метод create сериализатора, чтобы при помощи полученных данных - получить необходимый
    # объект Schedule (с доктором и датой-временем посещения), а так же добавить услуги к создаваемому приему
    def create(self, validated_data):
        record = Schedule.objects.get(app_time=validated_data['date'], doctor=validated_data['doctor'])

        app = Appointment.objects.create(record=record, patient=validated_data['patient'])

        for service in validated_data['service']:
            app.service.add(service)

        return app


# class AppointmentPostSerializer(serializers.ModelSerializer):
#     # patient = PatientSerializer()
#     # record = ScheduleSerializer()
#     # service = PriceSerializer()
#     date = serializers.DateField()
#     doctor = DoctorSerializer()
#
#     class Meta:
#         model = Appointment
#         fields = ('patient', 'date', 'doctor', 'service')

    # def validate(self, data):
    #     print(data)
    #     if 'doctor' in data and 'date' in data:
    #         try:
    #             app_time = App_times.objects.get(id=data['date'])
    #             schedule = Schedule.objects.get(doctor=data['doctor'], app_time=app_time)
    #         except(App_times.DoesNotExist, Schedule.DoesNotExist):
    #             raise serializers.ValidationError('Некорректно выбраны врач или дата посещения')
    #
    #         data['record'] = schedule.id
    #     else:
    #         raise serializers.ValidationError('Не выбраны врач или дата посещения')
    #     return data


class MedCardSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id', 'diagnosis', 'doctor', 'date')

    def get_doctor(self, app):
        return app.record.doctor.name + ' ' + app.record.doctor.surname

    def get_date(self, app):
        return app.record.app_time.date


class QuerySet1Serializer(serializers.Serializer):
    record__doctor__surname = serializers.CharField()
    amount = serializers.IntegerField()



class QuerySet2Serializer(serializers.Serializer):
    amount = serializers.IntegerField()
    doctor = serializers.CharField()

    class Meta:
        model = Appointment
        fields = ("amount", "doctor")


class QuerySet3Serializer(serializers.Serializer):
    amount = serializers.IntegerField()
    record__app_time__date = serializers.DateField()

    # class Meta:
    #     model = Appointment
    #     fields = ("amount", "date")
