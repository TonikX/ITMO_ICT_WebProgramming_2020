from django.shortcuts import render, redirect
from auto_racing_scoreboard.models import Car, Team, Racer, Race, Comment
from .forms import AddCommentForm, Registration
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'main_page.html')


def scoreboard(request):
    races = Race.objects.all()
    winners = [race.winner for race in races]
    racers = Racer.objects.filter(name__in=winners)
    cars_names = [racer.car for racer in racers]
    cars = Car.objects.filter(description__in=cars_names)
    return render(request, 'scoreboard.html', {'info': zip(races, racers, cars)})


def comments(request):
    comments = {}
    cm = Comment.objects.all()
    comments['comments'] = cm

    form = AddCommentForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        form.user = request.user
        form.save()
        return redirect('comments')
    comments['form'] = form

    return render(request, 'comments.html', comments)


def reg(request):
    form = Registration(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/registration.html', {'form': form})


class LogoutFormView(FormView):

    def get(self, request):
        logout(request)
        return redirect('/')