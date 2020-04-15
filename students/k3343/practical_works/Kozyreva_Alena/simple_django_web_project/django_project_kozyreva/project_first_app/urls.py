"""django_project_kozyreva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('time/', views.geeks_view),
    path('all_owners/', views.owners_list),
    path('all_cars/', views.CarList.as_view(template_name="cars.html")),
    path('add_owners/', views.create_view),
    path('add_cars/', views.CarCreate.as_view(template_name="create_car.html"))
]

