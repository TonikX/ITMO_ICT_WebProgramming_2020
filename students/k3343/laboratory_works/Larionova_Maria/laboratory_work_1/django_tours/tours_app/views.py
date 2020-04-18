from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
class TourView(ListView):
    model = Tour

    def get(self, request):
        context = {}

        try:
            context["tours"] = Tour.objects.all()
        except Tour.DoesNotExist:
            raise Http404("Tour does not exist")

        return render(request, 'tours.html', context)


@login_required
def about_tour(request, tour_id):

    try:
        tour = Tour.objects.get(pk=tour_id)

    except Tour.DoesNotExist:
        raise Http404("Tour does not exist")

    try:

    	comments = TourComment.objects.filter(tour=tour_id).all()

    except TourComment.DoesNotExist:
        print("There are no comments")

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
    registered = False

    if request.method == 'POST':

        register_user_form = UserForm(data=request.POST)

        if register_user_form.is_valid():

            user = register_user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:

            print(register_user_form.errors)
    else:

        register_user_form = UserForm()

    return render(request,'reg.html', {'register_user_form': register_user_form, 'registered': registered})


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
                return HttpResponse("Your account was inactive.")

        else:
            return HttpResponse("Incorrect pair login/password")

    else:
        return render(request, 'auth.html', {})
