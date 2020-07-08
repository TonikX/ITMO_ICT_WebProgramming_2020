from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name="luchapp"

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('request/new/', CreateRequestView.as_view()),
    path('request/<int:pk>', GetRequestView.as_view()),
    path('request/all', GetRequestsView.as_view()),
    path('client/new', CreateClientView.as_view()),
    path('client/all', GetClientsView.as_view()),
    path('company/new', CreateCompanyView.as_view()),
    path('payment/new', CreatePaymentView.as_view()),
    path('payment/<int:pk>', GetPaymentView.as_view()),
    path('payment/all', GetPaymentsView.as_view()),
    path('service/<int:pk>', GetServiceView.as_view()),
    path('service/all', GetServicesView.as_view()),
    path('gethead/', GetHeadView.as_view()),
    path('getclient/', GetClientView.as_view()),
    path('request/adminfilter', AdminFilterView.as_view()),
    path('employee/all', GetEmployeesView.as_view()),
    path('product/all', GetProductsView.as_view()),
]
