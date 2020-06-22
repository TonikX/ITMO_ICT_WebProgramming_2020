from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .forms import CommentForm, LoginForm, UserRegistrForm
from django.utils import timezone
from races_table.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def table(request):
    try:
        context = {"drivers": Driver.objects.all(), "part": Participation.objects.all(), "cars": Car.objects.all()}
    except:
        raise Http404('Что-то не так!')
    return render(request, 'races_table/index.html', context)


def show_exp(request, dr_id):
    driver = Driver.objects.get(id=dr_id)
    part = Participation.objects.filter(driver__id=dr_id)
    race = Race.objects.all()
    return render(request, 'races_table/exp.html', context={'part': part, 'race': race, 'driver': driver})


def show_comments(request, dr_id):
    driver = Driver.objects.get(id=dr_id)
    comms = Comment.objects.filter(driver__id=dr_id)
    return render(request, 'races_table/all_comments.html', context={'comms': comms, 'driver': driver})


@login_required
def add_comment(request, dr_id):
    context = {}
    driver = Driver.objects.get(id=dr_id)
    context['driver'] = driver
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.date = timezone.now()
        comment.driver = driver
        comment.save()
    context['form'] = form
    return render(request, 'races_table/add_comment.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html')
    else:
        user_form = UserRegistrForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

