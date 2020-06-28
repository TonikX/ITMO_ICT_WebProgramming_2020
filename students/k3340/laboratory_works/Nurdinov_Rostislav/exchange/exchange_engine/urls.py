from django.urls import path
from . import views

urlpatterns = [
    path("jobseeker/", views.JobSeekerListView.as_view()),
    path("jobseeker/<int:pk>/", views.JobSeekerDetailView.as_view()),
    path("vacancy/", views.VacancyListView.as_view()),
    path("vacancy/<int:pk>", views.VacancyDetailView.as_view()),
    path("employer/", views.EmployerListView.as_view()),
    path("employer/<int:pk>", views.EmployerDetailView.as_view()),
]
