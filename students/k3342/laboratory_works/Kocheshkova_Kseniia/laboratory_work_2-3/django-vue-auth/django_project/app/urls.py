from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = 'app'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('librarians', LibrarianListView.as_view()),
    path('visitors', VisitorListView.as_view()),
    path('halls', HallListView.as_view()),
    path('books', BookListView.as_view()),
    path('accessory', AccessoryListView.as_view()),
    path('rents', RentListView.as_view()),
    path('ownerships', OwnershipListView.as_view()),
    path('rents/add', AddRentView.as_view()),
    path('ownerships/add', AddOwnershipView.as_view()),
    path('books/add', AddBookView.as_view()),
]
