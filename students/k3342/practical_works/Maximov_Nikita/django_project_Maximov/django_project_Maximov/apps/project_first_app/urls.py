from django.urls import path
from . import views
from .views import CarList, AddCar

urlpatterns = [
	path('owner/<int:owner_id>', views.about_owner),
	path('owner_list/', views.owner_list),
	path('car_list/', CarList.as_view()),
	path('add_owner/', views.add_owner),
	path('add_car/', AddCar.as_view()),
	]