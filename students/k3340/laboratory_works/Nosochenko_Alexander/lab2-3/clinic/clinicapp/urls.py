from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.DoctorListView.as_view()),
    path('doctor/<int:pk>/', views.DoctorEditView.as_view()),
    path('transaction/', views.TransactionListView.as_view()),
    path('transaction/<int:pk>/', views.TransactionEditView.as_view()),
    path('client/', views.ClientsListView.as_view()),
    path('client/<int:pk>/', views.ClientsEditView.as_view()),
    path('record/', views.RecordsListView.as_view()),
    path('record/<int:pk>/', views.RecordsEditView.as_view()),
    path('cabinet/', views.CabinetListView.as_view()),
    path('cabinet/<int:pk>/', views.CabinetEditView.as_view()),
    path('reception/', views.ReceptionListView.as_view()),
    path('reception/<int:pk>/', views.ReceptionEditView.as_view()),
    path('reviews/', views.ReviewsListView.as_view()),
    path('reviews/<int:pk>/', views.ReviewsEditView.as_view()),

]