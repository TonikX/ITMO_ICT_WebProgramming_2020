from django.urls import path
from . import views
urlpatterns = [
    path('<int:owner_id>/', views.detail),
]
