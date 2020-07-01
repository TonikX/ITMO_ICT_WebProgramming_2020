from django.contrib.auth.models import User
from rest_framework import generics

from .models import *
from .serializers import *


class ApplicationListView(generics.ListAPIView):
	serializer_class = ApplicationSerializer

	def get_queryset(self):
		queryset = Application.objects.all()

		get_params = self.request.query_params

		from_date = get_params.get('from_date', None)
		to_date = get_params.get('to_date', None)
		class_type = get_params.get('class', None)
		spec = get_params.get('spec', None)
		privelege_type = get_params.get('privelege', None)
		state = get_params.get('state', None)
		minimal_point = get_params.get('min', None)
		top = get_params.get('top', None)
		enrollee = get_params.get('enrollee', None)
		secretary = get_params.get('secretary', None)

		if from_date:
			queryset = queryset.filter(application_date__gte=from_date)

		if to_date:
			queryset = queryset.filter(application_date__lte=to_date)

		if class_type:
			queryset = queryset.filter(enrollee__class_type=class_type)

		if spec:
			queryset = queryset.filter(spec__id=spec)

		if privelege_type:
			queryset = queryset.filter(enrollee__privelege_type=privelege_type)

		if state:
			queryset = queryset.filter(state=state)

		if minimal_point:
			queryset = queryset.filter(spec__minimal_point__lte=minimal_point)

		if top:
			queryset = queryset.order_by('-enrollee__exam_profile')

		if enrollee:
			queryset = queryset.filter(enrollee__user__username=enrollee)

		if secretary:
			queryset = queryset.filter(secretary__user__username=secretary)

		return queryset


class ApplicationNewView(generics.CreateAPIView):
	queryset = Application.objects.all()
	serializer_class = CreateApplicationSerializer


class ApplicationView(generics.RetrieveUpdateAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer


class SpecListView(generics.ListAPIView):
	queryset = Spec.objects.all()
	serializer_class = SpecSerializer


class SpecView(generics.RetrieveAPIView):
	queryset = Spec.objects.all()
	serializer_class = SpecSerializer


class EnrolleeListView(generics.ListAPIView):
	serializer_class = EnrolleeSerializer

	def get_queryset(self):
		queryset = Enrollee.objects.all()

		get_params = self.request.query_params

		username = get_params.get('username', None)

		if username:
			queryset = queryset.filter(user__username=username)

		return queryset


class EnrolleeNewView(generics.CreateAPIView):
	queryset = Enrollee.objects.all()
	serializer_class = CreateEnrolleeSerializer


class EnrolleeView(generics.RetrieveUpdateAPIView):
	queryset = Enrollee.objects.all()
	serializer_class = EnrolleeSerializer
