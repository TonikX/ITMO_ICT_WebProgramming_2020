from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.hotelsview, name='hotels'),
	path("hotel/<int:pk>/", views.allbthotel, name='hotel_detail'),
	path("register/", views.register, name="register"),
	path('', include("django.contrib.auth.urls")),
	path('add_comment/', views.addcomment, name='new_comment'),
]