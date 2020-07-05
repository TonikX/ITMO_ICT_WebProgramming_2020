from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dogs/', views.DogListView.as_view()),
    path('dogs/<int:pk>/', views.DogDetailView.as_view()),

    path('users/register/', views.RegistrationAPI.as_view(), name='register'),
    path('users/profile-info/', views.UserDetailedView.as_view(), name='profile-info'),

    path('clubs/', views.ClubListView.as_view()),

    path('experts/', views.ExpertListView.as_view()),

    path('shows/', views.ShowListView.as_view()),
    path('shows/<int:pk>/rings/', views.RingListView.as_view(), name='rings'),
    path('shows/<int:pk>/rings/<int:ring_id>/grades/', views.GradeListView.as_view()),

    path('registrations/', views.RegistrationListView.as_view()),

    path('performs/', views.PerformListView.as_view()),
]
