# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
     path('fix/', Fixes.as_view()),
     path('fix_add/', FixAdd.as_view()),
     path('fix_update/<int:pk>/', FixUpdate.as_view({'put': 'update'})),
     path('fix_filter/', FixFilter.as_view()),

     path('readers/', Readers.as_view()),
     path('reader/', ReaderOne.as_view()),
     path('reader_add/', ReaderAdd.as_view()),
     path('reader_del/<int:pk>/', ReaderDelUpd.as_view({'delete': 'destroy'})),
     path('reader_update/<int:pk>/', ReaderDelUpd.as_view({'post': 'update'})),
     path('readers_filter/', ReadersFilter.as_view()),

     path('books/', Books.as_view()),
     path('book/', BookOne.as_view()),
     path('book_add/', BookAdd.as_view()),
     path('book_del/<int:pk>/', BookDelUpd.as_view({'delete': 'destroy'})),
     path('book_update/<int:pk>/', BookDelUpd.as_view({'post': 'update'})),

     path('places/', Places.as_view()),
     path('place/', PlaceOne.as_view()),

     path('education/', EducationFiler.as_view()),

]