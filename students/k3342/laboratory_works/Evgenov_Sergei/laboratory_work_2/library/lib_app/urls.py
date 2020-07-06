from django.urls import path
from lib_app.views import *

urlpatterns = [
    path('hall/', Hall_V.as_view()),
    path('book/', Book_V.as_view()),
    path('reader_add/', Reader_V.as_view()),
    path('attachment/', Attachment_V.as_view()),
    path('reader/', Reader_books.as_view()),
    path('detach/<int:pk>/', Detach.as_view({'put': 'put'})),
    path('reader_change/<int:pk>/', Reader_change.as_view({'put': 'put'})),
    path('books/', Books_V.as_view()),
    path('reader_del/<int:pk>/', Reader_del.as_view()),
    path('book_add/', Book_add.as_view()),
    path('one_book/', Book_one.as_view()),
]
