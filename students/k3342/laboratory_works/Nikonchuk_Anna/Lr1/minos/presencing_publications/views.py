from .models import *
from .forms import *
from django.contrib.auth.models import User

import django.shortcuts
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .utils import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


class AboutList(ListView):
    model = DirectorDuties
    # directorduties_list.html

def authors_list(request):
    context = {"authors": Author.objects.all()}
    return django.shortcuts.render(request, 'presencing_publications/authors_board.html', context)
    # return django.shortcuts.render(request, 'presencing_publications/authors_board.html')


def author_detail(request, a_slug):
    author = Author.objects.get(a_slug__iexact=a_slug)
    return django.shortcuts.render(request, 'presencing_publications/author_detail.html', {'author': author})


class AuthorDetail(ObjectDetailMixin, View):
    def get(self, request, a_slug):
        author = get_object_or_404(Author, a_slug__iexact=a_slug)
        return django.shortcuts.render(request, 'presencing_publications/author_detail.html',
                                       context={'author': author, 'admin_object': author})


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
                                   {'book': book, 'publisher': publisher, 'authors': authors, 'admin_object': book})


def publishers_list(request):
    context = {'publishers': Publisher.objects.all()}
    return django.shortcuts.render(request, 'presencing_publications/publishers_board.html', context)


def publisher_detail(request, p_slug):
    publisher = Publisher.objects.get(p_slug__iexact=p_slug)
    return django.shortcuts.render(request,
                                   'presencing_publications/publisher_detail.html',
                                   {'publisher': publisher, 'admin_object': publisher})


class PublisherDetail(View):
    def get(self, request, p_slug):
        publisher = get_object_or_404(Publisher, p_slug__iexact=p_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/publisher_detail.html',
                                       context={'publisher': publisher, 'admin_object': publisher})


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


class PublisherUpdate(View):
    def get(self, request, p_slug):
        publisher = Publisher.objects.get(p_slug__iexact=p_slug)
        bound_form = PublisherForm(instance=publisher)
        return django.shortcuts.render(request,
                                       'presencing_publications/publisher_update.html',
                                       context={'form': bound_form, 'publisher': publisher})

    def post(self, request, p_slug):
        publisher = Publisher.objects.get(p_slug__iexact=p_slug)
        bound_form = PublisherForm(request.POST, instance=publisher)

        if bound_form.is_valid():
            new_publisher = bound_form.save()
            return django.shortcuts.redirect(new_publisher)
        return django.shortcuts.render(request,
                                       'presencing_publications/publisher_update.html',
                                       context={'form': bound_form, 'publisher': publisher})


class PublisherDelete(View):
    def get(self, request, p_slug):
        publisher = Publisher.objects.get(p_slug__iexact=p_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/publisher_delete.html',
                                       context={'publisher': publisher})

    def post(self, request, p_slug):
        publisher = Publisher.objects.get(p_slug__iexact=p_slug)
        publisher.delete()
        return django.shortcuts.redirect(reverse('publishers_board_url'))


class DirectorCreate(View):
    def get(self, request):
        form = DirectorForm()
        return django.shortcuts.render(request, 'presencing_publications/director_create.html', context={'form': form})

    def post(self, request):
        bound_form = DirectorForm(request.POST)

        if bound_form.is_valid():
            new_director = bound_form.save()
            return django.shortcuts.redirect('about_people_url')
        return django.shortcuts.render(request, 'presencing_publications/director_create.html',
                                       context={'form': bound_form})


class AuthorCreate(View):

    def get(self, request):
        form = AuthorForm()
        return django.shortcuts.render(request, 'presencing_publications/author_create.html', context={'form': form})

    def post(self, request):
        bound_form = AuthorForm(request.POST)

        if bound_form.is_valid():
            new_author = bound_form.save()
            return django.shortcuts.redirect('author_detail_url', new_author.a_slug)
        return django.shortcuts.render(request, 'presencing_publications/author_create.html', {'form': bound_form})


class AuthorUpdate(View):
    def get(self, request, a_slug):
        author = Author.objects.get(a_slug__iexact=a_slug)
        bound_form = AuthorForm(instance=author)
        return django.shortcuts.render(request,
                                       'presencing_publications/author_update.html',
                                       context={'form': bound_form, 'author': author})

    def post(self, request, a_slug):
        author = Author.objects.get(a_slug__iexact=a_slug)
        bound_form = AuthorForm(request.POST, instance=author)

        if bound_form.is_valid():
            new_author = bound_form.save()
            # return django.shortcuts.redirect(new_author)
            return django.shortcuts.redirect('author_detail_url', new_author.a_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/author_update.html',
                                       context={'form': bound_form, 'author': author})


class AuthorDelete(View):

    def get(self, request, a_slug):
        author = Author.objects.get(a_slug__iexact=a_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/author_delete.html',
                                       context={'author': author})

    def post(self, request, a_slug):
        author = Author.objects.get(a_slug__iexact=a_slug)
        author.delete()
        return django.shortcuts.redirect(reverse('authors_board_url'))


class BookCreate(View):

    def get(self, request):
        form = BookForm()
        return django.shortcuts.render(request, 'presencing_publications/book_create.html', context={'form': form})

    def post(self, request):
        bound_form = BookForm(request.POST)

        if bound_form.is_valid():
            new_book = bound_form.save()
            return django.shortcuts.redirect('book_detail_url', new_book.b_slug)
        return django.shortcuts.render(request, 'presencing_publications/book_create.html', {'form': bound_form})


class BookUpdate(View):
    def get(self, request, b_slug):
        book = Book.objects.get(b_slug__iexact=b_slug)
        bound_form = BookForm(instance=book)
        return django.shortcuts.render(request,
                                       'presencing_publications/book_update.html',
                                       context={'form': bound_form, 'book': book})

    def post(self, request, b_slug):
        book = Book.objects.get(b_slug__iexact=b_slug)
        bound_form = BookForm(request.POST, instance=book)

        if bound_form.is_valid():
            new_book = bound_form.save()
            return django.shortcuts.redirect('book_detail_url', new_book.b_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/book_update.html',
                                       context={'form': bound_form, 'book': book})


class BookDelete(View):

    def get(self, request, b_slug):
        book = Book.objects.get(b_slug__iexact=b_slug)
        return django.shortcuts.render(request,
                                       'presencing_publications/book_delete.html',
                                       context={'book': book})

    def post(self, request, b_slug):
        book = Book.objects.get(b_slug__iexact=b_slug)
        book.delete()
        return django.shortcuts.redirect(reverse(''))


@login_required
class AddCommentView(CreateView):
    model = Comment
    fields = ['user', 'type', 'place_author', 'place_book', 'place_publisher', 'place_shop', 'content', 'date']

    def as_view(request):
        comments = {}
        form = AddCommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return django.shortcuts.HttpResponseRedirect(reverse_lazy('all_comments'))
        comments['form'] = form
        return django.shortcuts.render(request, 'add_comment.html', comments)


"""
class UserCreate(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'type_user', 'photo', 'uniq_num', 'location', 'nationality']
    form = UserForm
"""


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('user_registration_url')
    success_msg = 'User was successfully created'

    def form_valid(self,  form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


"""
# Изменить пароль
u = User.objects.get(username='john')
u.set_password('new password')
u.save()
"""


class UserRegistrationView(CreateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'type_user', 'photo', 'uniq_num', 'location', 'nationality']
    success_msg = 'The user profile is successfully completed'

    def as_view(request):
        sn_user = {}
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.isu = request.user
            form.save()
            return django.shortcuts.HttpResponseRedirect(reverse_lazy('index'))
        sn_user['form'] = form
        return django.shortcuts.render(request, 'registration/profile_page.html', sn_user)


# login поставляемый используется
def authView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

"""
def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/")

# то же самое без перенаправление требует перенаправления
def logout_view(request):
    logout(request)
    # Redirect to a success page.


class LogoutView(FormView):
    def get(self, request):
        logout(request)
        return django.shortcuts.redirect('/')
"""
