from rest_framework import serializers
from .models import *

class DocumentSerializer(serializers.ModelSerializer):
	class Meta():
		model = Document
		fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
	class Meta():
		model = Exam
		fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
	class Meta():
		model = Certificate
		fields = '__all__'


class EnrolleeSerializer(serializers.ModelSerializer):
	school_class = serializers.CharField(source='get_school_class_display')
	privelege = serializers.CharField(source='get_privelege_display')
	documents = DocumentSerializer()
	exams = ExamSerializer()
	certificate_avg = CertificateSerializer()

	class Meta():
		model = Enrollee
		fields = '__all__'


class CreateEnrolleeSerializer(serializers.ModelSerializer):
	class Meta():
		model = Enrollee
		fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
	class Meta():
		model = Faculty
		fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
	faculty = FacultySerializer()

	class Meta():
		model = Department
		fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
	class Meta():
		model = Specialization
		fields = '__all__'


class SpecializationRealiseSerializer(serializers.ModelSerializer):
	department = FacultySerializer()
	specialization = SpecializationSerializer()

	class Meta():
		model = SpecializationRealise
		fields = '__all__'


class SecretarySerializer(serializers.ModelSerializer):
	faculty = FacultySerializer()

	class Meta():
		model = Secretary
		fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
	secretary = SecretarySerializer()
	specialization = SpecializationSerializer()
	enrollee = EnrolleeSerializer()
	state = serializers.CharField(source='get_state_display')
	education_form = serializers.CharField(source='get_education_form_display')

	class Meta():
		model = Application
		fields = '__all__'


class CreateApplicationSerializer(serializers.ModelSerializer):
	class Meta():
		model = Application
		fields = '__all__'
