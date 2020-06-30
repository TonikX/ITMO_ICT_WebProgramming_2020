from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>', show_owner),
    path('auto/', AutoView.as_view()),
    path('owner/all', onwer_list),
    path('owner/new', new_owner),
    path('auto/new', NewAuto.as_view(success_url='/auto/'))
]
