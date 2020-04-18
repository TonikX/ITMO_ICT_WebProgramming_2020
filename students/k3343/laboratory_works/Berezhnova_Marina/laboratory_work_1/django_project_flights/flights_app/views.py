from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

class FlightView(ListView):
    model = FlightActivities

    def get(self, request):
        context = {}

        try:
            context["flights"] = FlightActivities.objects.all()
        except Flight.DoesNotExist:
            raise Http404("Flight does not exist")

        return render(request, 'flight_list.html', context)


@login_required
def show_flight(request, flight_id):
    try:
        flight = FlightActivities.objects.get(pk=flight_id)
    except Flights.DoesNotExist:
        raise Http404("Flight does not exist")

    try:
    	comments = FlightComments.objects.filter(flight=flight_id).all()
    except FlightComments.DoesNotExist:
        pass

    form = CommentForm(request.POST)

    if request.POST.get('author_id') != None:
	    author_id = int(request.POST.get('author_id'))

    if form.is_valid():
        com_form = form.save(commit=False)
        com_form.post = form
        com_form.flight_id = flight_id
        com_form.author_id = author_id
        com_form.save()
        return HttpResponseRedirect('/flights/{}/'.format(flight_id))

    return render(request, 'flight.html', {'flight': flight, 'form': form, 'comments': comments})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/flights/')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/flights/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
