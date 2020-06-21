from django.urls import path
from . import views


urlpatterns = [
    path('owner/<int:owner_id>/', views.detail, name='detail'),
    path('blog/', views.post_list, name='post_list'),
    path('time/', views.geeks_view),
    path('create_owner/', views.ownerform),
    path('create_car/', views.CreateCar.as_view(template_name="carform.html")),
]