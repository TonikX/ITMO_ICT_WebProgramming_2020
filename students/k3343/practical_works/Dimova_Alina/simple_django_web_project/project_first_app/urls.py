from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>', views.show_owner),
    path('owners/', views.show_all_owners),
    path('cars/', views.CarList.as_view(template_name='auto_list.html')),
    path('owners_view/', views.create_view),
    path('cars_view/', views.AutoCreate.as_view(template_name='cars_form.html', success_url='/cars_view/')),
]
