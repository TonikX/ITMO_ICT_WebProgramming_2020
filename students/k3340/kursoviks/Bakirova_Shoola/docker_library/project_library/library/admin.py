from django.contrib import admin
from .models import Book, Place, Reader, Fix


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'library_card', 'education')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'section', 'cipher')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')


class FixAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'date_fix', 'handed', 'place')


admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Fix, FixAdmin)

