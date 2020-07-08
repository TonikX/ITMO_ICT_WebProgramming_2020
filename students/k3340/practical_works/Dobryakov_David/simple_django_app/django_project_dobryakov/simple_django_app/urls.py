from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('auto', views.AutoView.as_view()),
        path('owner/<int:owner_id>', views.show_owner),
        path('owners', views.show_owners),
        path('add_auto', views.AddAuto.as_view(success_url='thanks')),
        path('thanks', views.show_thanks),
        path('add_owner', views.add_owner)
]
