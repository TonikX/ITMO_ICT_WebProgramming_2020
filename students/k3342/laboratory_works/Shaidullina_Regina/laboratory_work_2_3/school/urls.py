from django.urls import path
from school.views import *


urlpatterns = [
    path('subjects/', Subjects.as_view()),
    path('rooms/', Rooms.as_view()),
    # path('rooms_sub/', RoomsWithSubject.as_view()),
    path('teachers/', Teachers.as_view()),
    path('teacher/', TeacherOne.as_view()),
    path('pupils/', Pupils.as_view()),
    path('pupil/', PupilOne.as_view()),
    path('classes/', Classes.as_view()),
    path('assessments/', Assessments.as_view()),
    path('assessment/', AssessmentOne.as_view()),
    path('timetable/', Timetables.as_view()),
    path('teaching/', Teachings.as_view()),
    path('query1/', Query1.as_view()),
    path('query2/', Query2.as_view()),
    path('query3/', Query3.as_view()),
    path('query4/', Query4.as_view()),
    path('query5/', Query5.as_view()),
    path('assessments_reports/', Report.as_view())
]
