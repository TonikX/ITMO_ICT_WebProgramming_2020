from django.urls import path
from alpinism.views import *

urlpatterns = [
    path('countries/', CountryView.as_view()),
    path('alpinists/', AlpinistView.as_view()),
    path('clubs/', ClubView.as_view()),
    path('mountains/', MountainView.as_view()),
    path('groups/', GroupView.as_view()),
    path('successes/', IndSuccessView.as_view()),
    path('ascents/', AscentView.as_view()),
    path('emergencies/', EmergencyView.as_view()),
    path('request1/', Request1View.as_view()),
    path('request2/', Request2View.as_view())
    ]
