from django.urls import path

from .views import *


app_name = "airport"

urlpatterns = [
	path('flights', FlightsView.as_view()),
	path('challengers', ChallengersView.as_view()),
	path('companies', CompaniesView.as_view())
]
