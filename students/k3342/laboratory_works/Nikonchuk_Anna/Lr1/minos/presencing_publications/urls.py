from django.urls import path
from . import views
from .views import *
from minos.views import main_board
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', main_board, name='main_boar_url'),
    
    # path('presencing_publications/', main_board, name='main_board_url'),
    path('presencing_publications/', authors_list, name='authors_board_url'),
    path('authors/', authors_list, name='authors_board_url'),
    path('books/', books_list, name='books_board_url'),
    path('publishers/', publishers_list, name='publishers_board_url'),
    path('author/create/', AuthorCreate.as_view(), name='author_create_url'),
    path('authors/<str:a_slug>/', author_detail, name='author_detail_url'),
    path('authors/<str:a_slug>/update/', AuthorUpdate.as_view(), name='author_update_url'),
    path('authors/<str:a_slug>/delete/', AuthorDelete.as_view(), name='author_delete_url'),
    # path('authors/<str:a_slug>', AuthorDetail.as_view, name='author_detail_url'),
    path('book/create/', BookCreate.as_view(), name='book_create_url'),
    path('books/<str:b_slug>/', book_detail, name='book_detail_url'),
    path('books/<str:b_slug>/update/', BookUpdate.as_view(), name='book_update_url'),
    path('books/<str:b_slug>/delete/', BookDelete.as_view(), name='book_delete_url'),
    path('publisher/create/', PublisherCreate.as_view(), name='publisher_create_url'),
    path('publishers/<str:p_slug>/', publisher_detail, name='publisher_detail_url'),
    path('publishers/<str:p_slug>/update/', PublisherUpdate.as_view(), name='publisher_update_url'),
    path('publishers/<str:p_slug>/delete/', PublisherDelete.as_view(), name='publisher_delete_url'),
    path('director/create/', DirectorCreate.as_view(), name='director_create_url'),
    path('about/', AboutList.as_view(), name='about_people_url'),

    # path('user/create', UserCreate.as_view(), name='user_create_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', views.LogoutView.as_view(), name='logout_url'),
    path('register/', UserRegistrationView.as_view, name='user_registration_url')
]

