from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register('teachers', views.TeachersViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/', views.StudentsListCreateView.as_view()),
    path('shedule/', views.SheduleListCreateView.as_view()),
    path('shedule/delete/<int:pk>', views.SheduleDeleteView.as_view()),
    path('teachers/delete/<int:pk>', views.TeachersDeleteView.as_view()),
    path('record/', views.RecordListCreateView.as_view()),
    path('subjects/', views.SubjectsListView.as_view()),
    path('teachers/update/<int:pk>', views.TeachersUpdateView.as_view()),
    path('students/update/<int:pk>', views.StudentsUpdateView.as_view()),
    path('students/delete/<int:pk>', views.StudentsDeleteView.as_view()),


]
