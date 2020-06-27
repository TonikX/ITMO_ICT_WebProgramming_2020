from django.urls import path
from . import views

urlpatterns = [
    path("jobseeker/", views.JobSeekerListView.as_view()),
    path("vacancy/", views.VacancyListView.as_view()),
]
