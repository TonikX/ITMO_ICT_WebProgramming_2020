from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = "airport"

urlpatterns = [
	path('flights', FlightsView.as_view()),
	path('challengers', ChallengersView.as_view()),
	path('companies', CompaniesView.as_view()),
	path('user/ticket/', UserTicketView.as_view()),
	path('user/me/', GetUserView.as_view()),
	path('auth/', include('djoser.urls')),
	path('auth/token/', obtain_auth_token, name="token"),
]
