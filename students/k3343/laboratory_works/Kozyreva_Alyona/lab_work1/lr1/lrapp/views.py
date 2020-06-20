from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
import datetime
from .models import Homework, Student, Comment
from .forms import RegUserForm, StudentForm, CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


def start(request):
    return render(request, 'start.html')

def index(request):
    return render(request, 'index.html')

def board(request):
    """Вывод всех дз"""
    homeworks = {}
    homeworks["homeworks"] = Homework.objects.all()
    return render(request, "board.html", homeworks)

def comments_list(request):
    """Вывод всех комментов"""
    comments = {}
    comments["comments"] = Comment.objects.all()
    return render(request, "comments.html", comments)


class RegUserView(CreateView): ###
    model = User
    template_name = 'reg_user.html'
    form_class = RegUserForm
    success_url = reverse_lazy('reg_name')
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


def reg_name(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = StudentForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
        return HttpResponseRedirect(reverse_lazy('index'))
    context['form'] = form
    return render(request, "reg_name.html", context)


def comment(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CommentForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
        return HttpResponseRedirect(reverse_lazy('index'))
    context['form'] = form
    return render(request, "comment.html", context)






