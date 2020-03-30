from django.urls import path
from . import views
from .views import detail
from .views import list_view
from .views import all_owners_output
from .views import GeeksList
from .views import CarsList

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail),
    path('list_view/', views.list_view),
    path('all_owners_output/', views.all_owners_output),
    path('geekslist', GeeksList.as_view()),
    path('all_cars_output/', CarsList.as_view()),
]
