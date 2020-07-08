from django.contrib import admin
from .models import Book, ReadingRoom, Reader, BookPlace, TakingBook

admin.site.register(Book)
admin.site.register(ReadingRoom)
admin.site.register(Reader)
admin.site.register(BookPlace)
admin.site.register(TakingBook)
# Register your models here.
