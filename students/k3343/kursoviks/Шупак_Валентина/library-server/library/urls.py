from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.BookViewSet.as_view({'get': 'list'})),
    path("book/<int:pk>/", views.BookViewSet.as_view({'get': 'retrieve'})),
    path("book/create", views.BookViewSet.as_view({'post': 'create'})),
    path("book/<int:pk>/delete", views.BookViewSet.as_view({'delete': 'destroy'})),
    path("book/<int:pk>/update", views.BookViewSet.as_view({'post': 'update'})),

    path("reader/", views.ReaderViewSet.as_view({'get': 'list'})),
    path("reader/<int:pk>/", views.ReaderViewSet.as_view({'get': 'retrieve'})),
    path("reader/create", views.ReaderViewSet.as_view({'post': 'create'})),
    path("reader/<int:pk>/delete", views.ReaderViewSet.as_view({'delete': 'destroy'})),
    path("reader/<int:pk>/update", views.ReaderViewSet.as_view({'post': 'update'})),

    path("taking_book/", views.TakingBookViewSet.as_view({'get': 'list'})),
    path("taking_book/<int:pk>/", views.TakingBookViewSet.as_view({'get': 'retrieve'})),
    path("taking_book/create", views.TakingBookViewSet.as_view({'post': 'create'})),
    path("taking_book/<int:pk>/delete", views.TakingBookViewSet.as_view({'delete': 'destroy'})),
    path("taking_book/<int:pk>/update", views.TakingBookViewSet.as_view({'post': 'update'})),

    path("book_place/", views.BookPlaceViewSet.as_view({'get': 'list'})),
    path("book_place/<int:pk>/", views.BookPlaceViewSet.as_view({'get': 'retrieve'})),
    path("book_place/create", views.BookPlaceViewSet.as_view({'post': 'create'})),
    path("book_place/<int:pk>/delete", views.BookPlaceViewSet.as_view({'delete': 'destroy'})),
    path("book_place/<int:pk>/update", views.BookPlaceViewSet.as_view({'post': 'update'})),

    path("reading_room/", views.ReadingRoomViewSet.as_view({'get': 'list'})),
    path("reading_room/<int:pk>/", views.ReadingRoomViewSet.as_view({'get': 'retrieve'})),
    path('query1/', views.Query1.as_view()),
    path('query5/', views.Query5.as_view()),
    ]
