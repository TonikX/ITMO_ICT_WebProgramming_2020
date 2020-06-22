from django.urls import path
from . import views


urlpatterns = [
    path('owner/<int:owner_id>/', views.detail, name='detail'),
    path('blog/', views.post_list, name='post_list'),
    path('time/', views.geeks_view),
    path('all_owners/', views.owners_list),
    path('all_cars/', views.CarList.as_view(template_name="Cars_View.html")),
    path('create_owner/', views.create_owner),
    path('create_car/', views.CreateCar.as_view(template_name="Create_Car.html")),
]


