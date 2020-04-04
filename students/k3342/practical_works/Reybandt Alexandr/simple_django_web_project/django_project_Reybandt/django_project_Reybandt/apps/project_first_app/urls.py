from django.urls import path
from . import views
from .views import CarList, CreateCar

urlpatterns = [
	path('owner_info', views.info, name = 'info'),
	path('owner/<int:ownership_id>', views.detail, name = 'detail'),
	path('owners_list', views.owners_list),
	path('car_list', CarList.as_view()),
	path('', views.create_view),
	path('car_model', CreateCar.as_view()),
]
