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
    path('all_styles/', AllStyles.as_view()),
    path('teachers_for_style/', TeachersForStyle.as_view()),
    path('add_teachers_for_wsh/', AddTeachersForWSH.as_view()),
    path('report/', ProfitInfo.as_view()),
    path('all_teachers/', AllTeachers.as_view()),
    path('wsh_nearest/', NearestWshForTeacher.as_view()),
    path('wsh_filter/', FilteredWSH.as_view()),
    path('wsh_upd/<int:pk>/', UpdateWSH.as_view({'post':'update'})),
    path('one_part/', OnePart.as_view()),
]