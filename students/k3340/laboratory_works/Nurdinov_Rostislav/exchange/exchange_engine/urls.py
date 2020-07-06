from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path("jobseeker/list/", views.JobSeekerListView.as_view()),
    path("jobseeker/detail/<int:pk>/", views.JobSeekerRetrieveUpdateDeleteView.as_view()),
    path("jobseeker/create/", views.JobSeekerCreateView.as_view()),

    path("vacancy/list/", views.VacancyListView.as_view()),
    path("vacancy/detail/<int:pk>/", views.VacancyRetrieveUpdateDeleteView.as_view()),
    path("vacancy/create/", views.VacancyCreateView.as_view()),

    path("profession/list/", views.ProfessionListView.as_view()),
    path("profession/detail/<int:pk>/", views.ProfessionRetrieveUpdateDeleteView.as_view()),
    path("profession/create/", views.ProfessionCreateView.as_view()),

    path("employer/list/", views.EmployerListView.as_view()),
    path("employer/detail/<int:pk>", views.EmployerRetrieveUpdateDeleteView.as_view()),
    path("employer/create/", views.EmployerCreateView.as_view()),

    path("experience/list/<int:pk>/", views.ExperienceListView.as_view()),
    path("experience/detail/<int:pk>", views.ExperienceRetrieveUpdateDeleteView.as_view()),
    path("experience/create/", views.ExperienceCreateView.as_view()),

    path("resume/list/<int:pk>/", views.ResumeListView.as_view()),
    path("resume/detail/<int:pk>", views.ResumeRetrieveUpdateDeleteView.as_view()),
    path("resume/create/", views.ResumeCreateView.as_view()),

]
