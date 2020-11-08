import django.shortcuts
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View

'''
# doesn't work
class AuthorDetail(View):
    def get(self, request, a_slug):
        author = Author.objects.get(a_slug__iexact=a_slug)
        return django.shortcuts.render(request, 'presencing_publications/author_detail.html', {'author': author})
'''


class AboutList(ListView):
    model = DirectorDuties


def authors_list(request):
    context = {"authors": Author.objects.all()}
    return django.shortcuts.render(request, 'presencing_publications/authors_board.html', context)
    # return django.shortcuts.render(request, 'presencing_publications/authors_board.html')


def author_detail(request, a_slug):
    author = Author.objects.get(a_slug__iexact=a_slug)
    return django.shortcuts.render(request, 'presencing_publications/author_detail.html', {'author': author})


class AuthorDetail(View):
    def get(self, request, a_slug):
        author = get_object_or_404(Author, a_slug__iexact=a_slug)
        return django.shortcuts.render(request, 'presencing_publications/author_detail.html', context={'author': author})


def books_list(request):
    context = {'books': Book.objects.all()}
    return django.shortcuts.render(request, 'presencing_publications/books_board.html', context)


def book_detail(request, b_slug):
    book = Book.objects.get(b_slug__iexact=b_slug)
    try:
        publisher = Publisher.objects.get(name=book.publisher)
    except:
        publisher = None
    try:
        authors = book.authors.all()
    except:
        authors = [None]
    return django.shortcuts.render(request, 'presencing_publications/book_detail.html',
                                   {'book': book, 'publisher': publisher, 'authors': authors})


class BookDetail(View):
    def get(self, request, b_slug):
        book = get_object_or_404(Book, a_slug__iexact=b_slug)
        return django.shortcuts.render(request, 'presencing_publications/book_detail.html', context={'book': book})


def publishers_list(request):
    context = {'publishers': Publisher.objects.all()}
    return django.shortcuts.render(request, 'presencing_publications/publishers_board.html', context)


def publisher_detail(request, p_slug):
    publisher = Publisher.objects.get(p_slug__iexact=p_slug)
    return django.shortcuts.render(request, 'presencing_publications/publisher_detail.html', {'publisher': publisher})


class PublisherCreate(View):

    def get(self, request):
        form = PublisherForm()
        return django.shortcuts.render(request, 'presencing_publications/publisher_create.html', context={'form': form})

    def post(self, request):
        bound_form = PublisherForm(request.POST)  # получаем связанную форму (заполненные поля)

        if bound_form.is_valid():
            new_publisher = bound_form.save()
            return django.shortcuts.redirect(new_publisher)  # переходим на страницу созданного объекта
        # отображаем невалидную форму с ошибками
        return django.shortcuts.render(request, 'presencing_publications/publisher_create.html', {'form': bound_form})


class DirectorCreate(View):
    def get(self, request):
        form = DirectorForm()
        return django.shortcuts.render(request, 'presencing_publications/director_create.html', context={'form': form})

    def post(self, request):
        bound_form = DirectorForm(request.POST)

        if bound_form.is_valid():
            new_director = bound_form.save()
            return django.shortcuts.redirect(new_director)
        return django.shortcuts.render(request, 'presencing_publications/director_create.html', context={'form': bound_form})


class AuthorCreate(View):

    def get(self, request):
        form = AuthorForm()
        return django.shortcuts.render(request, 'presencing_publications/author_create.html', context={'form': form})

    def post(self, request):
        bound_form = AuthorForm(request.POST)

        if bound_form.is_valid():
            new_author = bound_form.save()
            return django.shortcuts.redirect(new_author)
        return django.shortcuts.render(request, 'presencing_publications/author_create.html', {'form': bound_form})


class BookCreate(CreateView):
    model = Book
    fields = ['orig_lang_title', 'orig_lang', 'trans_lang', 'title', 'editor', 'translator', 'narrator', 'illustrator', 'authors', 'publisher',  'publication_date', 'type_cover', 'cover', 'b_slug', 'b_ganre', 'descr']

