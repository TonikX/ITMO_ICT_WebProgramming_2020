from django.urls import path
from . import views

urlpatterns=[
    path('drivers/', views.DriverListView.as_view()),
    path('driver/<int:pk>/', views.DriverDetailView.as_view()),
    path('order/', views.OrderCreateView.as_view()),
    path('client/', views.YoungListView.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),
    path('order-list/', views.DriverOrderView.as_view()),
    path('week/', views.WeekDayOrderView.as_view()),
    path('top/', views.TopCategoryView.as_view()),
    path('storage_client/', views.StorageClientView.as_view()),
    path('new-driver/', views.DriverCreateView.as_view()),
    path('delete-driver/<int:pk>/', views.DriverDeleteView.as_view()),
    path('storage/', views.StorageView.as_view()),
    path('report/', views.ToFabricTrashView.as_view()),
    path('add_order/', views.OrderStorageCreateView.as_view()),
    path('delete-order/<int:pk>', views.OrderStorageDeleteView.as_view()),
]