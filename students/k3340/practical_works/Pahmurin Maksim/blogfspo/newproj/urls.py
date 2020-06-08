from django.urls import path
from .views import detail
from . import views

urlpatterns = [
    path('owner/<int:poll_id>/', detail),
    path('autoholders_list/', views.show_autoholders_list),
    path('auto_list/', views.AutoList.as_view(), name='auto_list'),
    path('auto_form/', views.AutoForm.as_view(success_url="/success/")),
    path('success/', views.success)
]