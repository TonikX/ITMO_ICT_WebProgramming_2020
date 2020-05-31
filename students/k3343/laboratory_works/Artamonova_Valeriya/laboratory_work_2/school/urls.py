from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("teacher/", views.TeacherViewSet.as_view({'get': 'list'})),
    path("teacher/<int:pk>/", views.TeacherViewSet.as_view({'get': 'retrieve'})),
    path("teacher/add", views.TeacherViewSet.as_view({'post': 'create'})),
    path("teacher/<int:pk>/update", views.TeacherViewSet.as_view({'post': 'update'})),
    path("teacher/<int:pk>/delete", views.TeacherViewSet.as_view({'delete': 'destroy'})),
    path("pupil/", views.PupilViewSet.as_view({'get': 'list'})),
    path("pupil/<int:pk>/", views.PupilViewSet.as_view({'get': 'retrieve'})),
    path("pupil/add", views.PupilViewSet.as_view({'post': 'create'})),
    path("pupil/<int:pk>/update", views.PupilViewSet.as_view({'post': 'update'})),
    path("pupil/<int:pk>/delete", views.PupilViewSet.as_view({'delete': 'destroy'})),
    path("grade/", views.GradeCreateView.as_view({'post': 'create'})),
    path("timetable/", views.TimetableViewSet.as_view({'get': 'list'})),
    path("timetable/add", views.TimetableViewSet.as_view({'post': 'create'})),
    path("klass/", views.KlassViewSet.as_view({'get': 'list'})),
    path("klass/<int:pk>/", views.KlassViewSet.as_view({'get': 'retrieve'})),
    path("klass/<int:pk>/delete", views.KlassViewSet.as_view({'delete': 'destroy'})),
    path("klass/add/", views.KlassViewSet.as_view({'post': 'create'})),
    path("subject/", views.SubjectViewSet.as_view({'get': 'list'})),
    path("cabinet/", views.CabinetViewSet.as_view({'get': 'list'})),
    ]

"""router = DefaultRouter()
router.register('teacher', views.TeacherView1)
urlpatterns = router.urls"""