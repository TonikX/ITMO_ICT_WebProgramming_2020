from django.urls import path
from . import views
from .views import output_conferences
from .views import conference_info
from .views import register
from .views import LoginFormView
from .views import LogoutView


urlpatterns = [
    path('output_conferences/', views.output_conferences, name="conf_output"),
    path('conference_info/<int:conf_id>/', views.conference_info, name='conf_info'),
    path('register/', views.register, name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]