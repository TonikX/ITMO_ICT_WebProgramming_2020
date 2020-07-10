from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *

# Create your views here.
class GetAllApplicationView(generics.ListAPIView):
	serializer_class = ApplicationSerializer

	def get_queryset(self):
		queryset = Application.objects.all()

		params = self.request.query_params

		specialization = params.get('specialization', None)
		date = params.get('date', None)
		state = params.get('state', None)
		education_form = params.get('education_form', None)
		school_class = params.get('school_class', None)
		exam = params.get('exam', None)
		enrollee = params.get('enrollee', None)

		if enrollee:
			queryset = queryset.filter(enrollee__id=enrollee)

		if specialization:
			queryset = queryset.filter(specialization__id=specialization)

		if date:
			queryset = queryset.filter(date=date)

		if state:
			queryset = queryset.filter(state=state)

		if education_form:
			queryset = queryset.filter(education_form=education_form)

		if school_class:
			queryset = queryset.filter(enrollee__school_class=school_class)

		if exam:
			queryset = queryset.order_by('enrollee__exams__profile_points')

		return queryset		


class GetAllSpecializationView(generics.ListAPIView):
	queryset = Specialization.objects.all()
	serializer_class = SpecializationSerializer


class GetApplicationView(generics.RetrieveAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer


class GetSpecializationView(generics.RetrieveAPIView):
	queryset = Specialization.objects.all()
	serializer_class = SpecializationSerializer


class CreateDocView(generics.CreateAPIView):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializer


class CreateExamView(generics.CreateAPIView):
	queryset = Exam.objects.all()
	serializer_class = ExamSerializer


class CreateCertView(generics.CreateAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer


class CreateEnrolleeView(generics.CreateAPIView):
	queryset = Enrollee.objects.all()
	serializer_class = CreateEnrolleeSerializer


class CreateApplicationView(generics.CreateAPIView):
	queryset = Application.objects.all()
	serializer_class = CreateApplicationSerializer
