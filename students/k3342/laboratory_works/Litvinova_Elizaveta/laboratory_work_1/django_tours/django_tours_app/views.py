from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


class TourView(ListView):
    model = Tour

    def get(self, request):
        context = {}

        try:
            context["tours"] = Tour.objects.all()
        except Tour.DoesNotExist:
            raise Http404("Туров не найдено.")

        return render(request, 'tours.html', context)


@login_required
def about_tour(request, tour_id):

    try:
        tour = Tour.objects.get(pk=tour_id)

    except Tour.DoesNotExist:
        raise Http404("Нет такого тура")

    try:

    	comments = Comment.objects.filter(tour=tour_id).all()

    except Comment.DoesNotExist:
        print("Не найдено комментариев")

    if request.POST.get('user_id'):
	    user_id = int(request.POST.get('user_id'))

    form = CommentForm(request.POST)

    if form.is_valid():

        tour_form = form.save(commit=False)

        tour_form.post = form
        tour_form.author_id = user_id
        tour_form.tour_id = tour_id

        tour_form.save()

        return HttpResponseRedirect('/tours/{}/'.format(tour_id))

    return render(request, 'tour.html', {'tour': tour, 'comments': comments, 'form': form})


def register(request):
    is_registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            is_registered = True

        else:

            print(user_form.errors)
    else:

        user_form = UserForm()

    return render(request,'register.html', {'user_form': user_form, 'is_registered': is_registered})


def auth(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/tours/')

            else:
                return HttpResponse("Ваш аккаунт пока неактивен, обратитесь к администратору.")

        else:
            return HttpResponse("Неверная пара логин/пароль.")

    else:
        return render(request, 'auth.html', {})
