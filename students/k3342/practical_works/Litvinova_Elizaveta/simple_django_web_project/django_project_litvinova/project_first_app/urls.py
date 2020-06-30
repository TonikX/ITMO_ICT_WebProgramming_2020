from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>', show_owner),
    path('auto/', AutoView.as_view()),

]
