from django.urls import path
from dances.views import *

urlpatterns = [
    path('part/', Part.as_view()),
    path('add_part/', Wsh.as_view()),
    path('not_incl/', NotInclPeople.as_view()),
    path('remove_part/', RemovePartic.as_view()),
    path('add_wsh/', CreateWSH.as_view()),
    path('halls_for_school/', HallsForSchool.as_view()),
    path('all_schools/', AllSchools.as_view()),
]