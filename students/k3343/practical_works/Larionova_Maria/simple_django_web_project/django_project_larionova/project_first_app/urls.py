from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:owner_id>', views.get_owner_info),
        path('owners/', views.get_owners_info),
        path('auto/', views.AutoInfoView.as_view()),
        path('create_owner/', views.create_owner),
        path('create_auto/', views.CreateAuto.as_view(success_url="/success")),
        path('success/', views.get_success)
]
