from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:owner_id>', views.owner_info),
        path('auto/', views.AboutAutoView.as_view()),
        path('owners/', views.owners_info),
        path('new_auto/', views.NewAuto.as_view(success_url="/new_auto/")),
        path('new_owner/', views.new_owner)
]
