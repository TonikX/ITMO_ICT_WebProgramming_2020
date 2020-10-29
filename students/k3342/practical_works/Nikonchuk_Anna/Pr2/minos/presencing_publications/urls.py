from django.urls import path

from minos.views import main_board
from .views import *


urlpatterns = [
    path('', main_board, name='main_boar_url'),
    # path('presencing_publications/', main_board, name='main_board_url'),
    path('presencing_publications/', authors_list, name='authors_board_url'),
    path('authors/', authors_list, name='authors_board_url'),
    path('books/', books_list, name='books_board_url'),
    path('publishers/', publishers_list, name='publishers_board_url'),
    # path('author/create/', AuthorCreate.as_view(), name='author_create_url'),
    path('authors/<str:a_slug>/', author_detail, name='author_detail_url'),
    # path('authors/<str:a_slug>', AuthorDetail.as_view, name='author_detail_url'),
    # path('book/create/', BookCreate.as_view(), name='book_create_url'),
    path('books/<str:b_slug>/', book_detail, name='book_detail_url'),
    path('publisher/create/', PublisherCreate.as_view(), name='publisher_create_url'),
    path('publishers/<str:p_slug>/', publisher_detail, name='publisher_detail_url'),
    path('director/create/', DirectorCreate.as_view(), name='director_create_url'),
    path('about/', AboutList.as_view()),
]

