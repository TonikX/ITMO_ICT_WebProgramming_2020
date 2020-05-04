from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from flights.models import Client, Flight, Comment
from .forms import RegisterUserForm, ClientRegister, AddComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def main(request):
    return render(request, 'main.html')


def show_flights(request):
    flights = {'flights': Flight.objects.all()}
    return render(request, 'flights_table.html', flights)


def show_comments(request):
    comments = {"comments": Comment.objects.all()}
    return render(request, 'all_comments.html', comments)


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class ClientRegistration(CreateView):
    model = Client
    fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'bonus_card']
    success_msg = 'Your profile is complete'

    def as_view(request):
        clients = {}
        form = ClientRegister(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        clients['form'] = form
        return render(request, 'registration/profile_page.html', clients)


@login_required
class AddCommentClass(CreateView):
    model = Comment
    fields = ['flight', 'comment_type', 'text']

    def as_view(request):
        comments = {}
        form = AddComment(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('all_comments'))
        comments['form'] = form
        return render(request, 'add_comment.html', comments)
