from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.TeacherViewSet.as_view({'get': 'list'})),
    path("teacher/<int:pk>/", views.TeacherViewSet.as_view({'get': 'retrieve'})),
    path("teacher/add", views.TeacherViewSet.as_view({'post': 'create'})),
    path("teacher/<int:pk>/update", views.TeacherViewSet.as_view({'post': 'update'})),
    path("teacher/<int:pk>/delete", views.TeacherViewSet.as_view({'delete': 'destroy'})),
    path("children/", views.ChildrenViewSet.as_view({'get': 'list'})),
    path("children/<int:pk>/", views.ChildrenViewSet.as_view({'get': 'retrieve'})),
    path("children/add", views.ChildrenViewSet.as_view({'post': 'create'})),
    path("children/<int:pk>/update", views.ChildrenViewSet.as_view({'post': 'update'})),
    path("children/<int:pk>/delete", views.ChildrenViewSet.as_view({'delete': 'destroy'})),
    path("grade/", views.GradeViewSet.as_view({'post': 'create'})),
    path("grade/<int:pk>/delete", views.GradeViewSet.as_view({'delete': 'destroy'})),
    path("grade/<int:pk>/update", views.GradeViewSet.as_view({'post': 'update'})),
    path("timetable/", views.TimetableViewSet.as_view({'get': 'list'})),
    path("timetable/<int:pk>", views.TimetableViewSet.as_view({'get': 'retrieve'})),
    path("timetable/add", views.TimetableViewSet.as_view({'post': 'create'})),
    path("timetable/<int:pk>/delete", views.TimetableViewSet.as_view({'delete': 'destroy'})),
    path("timetable/<int:pk>/update", views.TimetableViewSet.as_view({'post': 'update'})),
    path("nclass/", views.NclassViewSet.as_view({'get': 'list'})),
    path("nclass/<int:pk>/", views.NclassViewSet.as_view({'get': 'retrieve'})),
    path("nclass/<int:pk>/delete", views.NclassViewSet.as_view({'delete': 'destroy'})),
    path("nclass/add/", views.NclassViewSet.as_view({'post': 'create'})),
    path("subject/", views.SubjectViewSet.as_view({'get': 'list'})),
    path("room/", views.RoomViewSet.as_view({'get': 'list'})),
]
