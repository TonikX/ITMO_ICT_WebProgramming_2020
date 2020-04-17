from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from .forms import CommentForm

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

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/flights/{}/'.format(flight_id))

    return render(request, 'flight.html', {'flight': flight, 'form': form, 'comments': comments})
