from django.urls import path
from . import views
from .views import CarList

urlpatterns = [
	path('', views.info, name = 'info'),
	path('owner/<int:ownership_id>', views.detail, name = 'detail'),
	path('owners_list', views.owners_list),
	path('car_list', CarList.as_view()),
]
