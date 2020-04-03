"""django_project_Shaidullina URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from project_first_app import views
from project_first_app.views import CarsList, CarCreate


urlpatterns = [
    path('', include('project_first_app.urls')),
    path('admin/', admin.site.urls),
    path('query/', views.query),
    path('owners/', views.all_owners),
    path('cars/', CarsList.as_view()),
    path('func_form/', views.input_owners),
    path('class_form/', CarCreate.as_view(success_url="/class_form/"))
]
