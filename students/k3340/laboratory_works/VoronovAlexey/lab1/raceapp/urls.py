"""lab1 URL Configuration

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
from django.urls import path, include
from raceapp import views, forms

urlpatterns = [
    path('results', views.results),
    path('result/<int:id>/', views.result),
    path('addrace', views.raceform),
    path('addresult', views.addresult),
    path('comments/<int:id>/', views.comments),
#    path('add_comment/<int:id>/', forms.AddVehicle.as_view()),
    path('', views.results),
]
