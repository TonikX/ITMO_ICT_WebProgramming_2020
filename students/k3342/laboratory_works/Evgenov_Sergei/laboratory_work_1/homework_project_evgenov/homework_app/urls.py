from django.urls import path
from . import views

urlpatterns = [
    path('homework/<int:homework_id>', views.homework),
    path('homework/list_view', views.HomeworkList.as_view())
]