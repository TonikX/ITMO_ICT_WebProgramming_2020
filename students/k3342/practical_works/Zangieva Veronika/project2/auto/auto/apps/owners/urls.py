from django.urls import path

from . import views

#from .views import index

#from .views import CarsList
#from .views import create_view
from .views import CarsCreate

urlpatterns = [
	#Функционально
	#path('', views.index, name = 'index'),
	#На основе классов 
	#path('', CarsList.as_view())
	#Форма функционально
	#path('', views.create_view, name = 'create_view')
	#Форма на основе классов
	path('', CarsCreate.as_view()),


	#path('<int:owner_id>/', views.detail, name = 'detail'),
] 