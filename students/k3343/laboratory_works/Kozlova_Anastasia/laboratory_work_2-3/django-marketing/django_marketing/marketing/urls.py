from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


app_name = "marketing"

urlpatterns = [
	path('company/new', CreateCompanyView.as_view()),
	path('company/all', GetCompaniesView.as_view()),
	path('client/new', CreateClientView.as_view()),
	path('client/all', GetClientsView.as_view()),
	path('request/new', CreateRequestView.as_view()),
	path('request/all', GetRequestsView.as_view()),
	path('request/<int:pk>', GetRequestView.as_view()),
	path('request/service', CreateServiceForRequestView.as_view()),
	path('request/service/all', GetServiceForRequestView.as_view()),
	path('product/new', CreateProductView.as_view()),
	path('product/all', GetProductsView.as_view()),
	path('product/<int:pk>', GetProductView.as_view()),
	path('payments/new', CreatePaymentView.as_view()),
	path('payments/all', GetPaymentsView.as_view()),
	path('payments/<int:pk>', GetPaymentView.as_view()),
	path('services/all', GetServicesView.as_view()),
	path('services/<int:pk>', GetServiceView.as_view()),
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token'),
	path('is/client', IsClientView.as_view()),
	path('is/employee', IsEmployeeView.as_view()),
]
