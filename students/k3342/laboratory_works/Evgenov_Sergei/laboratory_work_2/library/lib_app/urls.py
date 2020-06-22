from django.urls import path
from lib_app.views import *

urlpatterns = [
    path('hall/', Hall_V.as_view()),
    path('book/', Book_V.as_view()),
    path('reader_old/', Reader_V.as_view()),
    path('attachment/', Attachment_V.as_view()),
    path('reader/', Reader_books.as_view()),
]
