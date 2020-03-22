from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.detail, name='detail'),
    path('blog/', views.post_list, name='post_list')
]
