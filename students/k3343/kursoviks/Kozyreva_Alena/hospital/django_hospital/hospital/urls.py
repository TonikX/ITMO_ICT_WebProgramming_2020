from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = "hospital"

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token'),

	path('patients/', GetAllPatientView.as_view()),
	path('patients/cards', GetAllPatientCardView.as_view()),
	path('doctors/', GetAllDoctorView.as_view()),
	path('appointments/', GetAllAppointmentView.as_view()),
	path('payments/', GetAllPaymentView.as_view()),
	path('prices/', GetAllPriceView.as_view()),
	path('appointments/<int:pk>', UpdateAppointmentView.as_view()),
	path('payments/<int:pk>', UpdatePaymentView.as_view()),
	path('appointments/add/', CreateAppointmentView.as_view()),
	path('payments/add/', CreatePaymentView.as_view()),
	path('doctors/add/', CreateDoctorView.as_view()),
	path('patients/add/', CreatePatientView.as_view()),
	path('patients/cards/add/', CreatePatientCardView.as_view()),
	path('patients/cards/<int:pk>', UpdatePatientCardView.as_view()),

]
