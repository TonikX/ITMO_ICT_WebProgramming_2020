from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
        path('owner/<int:owner_id>', views.show_owner),
        path('list_owners/', views.show_list_owners),
        path('list_auto/', views.ShowAuto.as_view(), name='list_auto'),
        path('owner_view/', views.owner_view),
        path('auto_form/', views.AutoForm.as_view(success_url="/success/")),
        path('success/', views.success)
]
