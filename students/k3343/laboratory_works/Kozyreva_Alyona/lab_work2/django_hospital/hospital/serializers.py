from rest_framework import serializers
from .models import *


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = '__all__'


class PatientCardSerializer(serializers.ModelSerializer):
	# patient = PatientSerializer()

	class Meta:
		model = PatientCard
		fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
	gender = serializers.CharField(source='get_gender_display')

	class Meta:
		model = Doctor
		fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
	patient = PatientSerializer()
	doctor = DoctorSerializer()

	class Meta:
		model = Appointment
		fields = '__all__'


class CreateAppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
	appointment = AppointmentSerializer()

	class Meta:
		model = Payment
		fields = '__all__'


class CreatePaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
	doctor = DoctorSerializer()

	class Meta:
		model = Price
		fields = '__all__'


class CalendarSerializer(serializers.ModelSerializer):
	day_type = serializers.CharField(source='get_day_type_display')
	doctor = DoctorSerializer()

	class Meta:
		model = Calendar
		fields = '__all__'


class CabinetSerializer(serializers.ModelSerializer):
	doctor = DoctorSerializer()

	class Meta:
		model = Cabinet
		fields = '__all__'


class CreateDoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = '__all__'

