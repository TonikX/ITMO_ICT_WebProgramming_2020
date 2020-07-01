from django.shortcuts import render, redirect
from django.http import Http404
from main_interface.models import Conference
from main_interface.models import Conference_themes
from main_interface.models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, CommentForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
import datetime


def output_conferences(request):
    context = {}
    context["dataset"] = Conference.objects.all()
    return render(request, "output_conferences.html", context)


def conference_info(request, conf_id):
    context = {}
    conf = Conference.objects.get(pk=conf_id)
    context["conf"] = conf

    context["themes_id"] = Conference_themes.objects.filter(conference=conf_id)
    context["comments"] = Comment.objects.filter(conference=conf_id).order_by('date')

    form = CommentForm(request.POST)
    context['form'] = form
    if form.is_valid():
        object = form.save(commit=False)
        object.conference = conf
        object.user = request.user
        object.date = datetime.datetime.now()
        object.save()
        return redirect('/conference_info/'+str(conf_id))

    return render(request, "conference_info.html", context)


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('/output_conferences/')
    return render(request, 'register.html', {'form': form})


class LoginFormView(FormView):

    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/output_conferences/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/output_conferences/")


