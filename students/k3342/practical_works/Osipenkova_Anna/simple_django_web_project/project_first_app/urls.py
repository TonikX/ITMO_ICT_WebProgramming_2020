from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:owner_id>/', views.detail),
    path('auto/', views.AutoView.as_view()),
    path('owners/', views.get_owners),
    path('new_auto/', views.NewAuto.as_view(success_url="/new_auto/")),
    path('new_owner/', views.new_owner)
]