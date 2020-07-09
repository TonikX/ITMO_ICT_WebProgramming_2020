from django.urls import path
from .views import output


urlpatterns = [
	path('owner/<int:owner_id>', output, name='output')
]
