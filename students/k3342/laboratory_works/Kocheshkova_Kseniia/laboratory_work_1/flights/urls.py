"""laboratory_work_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views


urlpatterns = [
    path('person/<int:person_id>/', views.person_info),
    path('person_list', views.person_list, name='person_list'),
    path('flights', views.flights, name='flights'),
    path('comments/<int:key>', views.comments, name='comments'),
    path('new_comment', views.NewCommentView.as_view, name='new_comment'),
    path('reservations/<int:key>', views.reservations, name='reservations'),
    path('new_reservation', views.NewReservationView.as_view, name='new_reservation'),
    path('register', views.RegisterView.as_view(), name='register')
]
