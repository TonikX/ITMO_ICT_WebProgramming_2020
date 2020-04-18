from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import Company, Direction, Gate, Flight, Comments
from django.views.generic.list import ListView
from .forms import CommentForm


def flights_list(request):
    """Список всех рейсов"""
    flights = Flight.objects.all().order_by('arrival')
    return render(request, "flightslist.html", {"flights": flights})

def flights_type(request, pk):
    """Фильтр рейсов в зависимости от типа (разделение на отлёты и прилёты)"""
    flights = Flight.objects.all()
    if pk == 1:
        flights = flights.order_by('arrival')
    elif pk == 2:
        flights = flights.filter(flighttype='D').order_by('departure')
    elif pk == 3:
        flights = flights.filter(flighttype='A').order_by('arrival')
    return render(request, "flightslist.html", {"flights": flights})

def flight_single(request, pk):
    """Вывод информации о конкретном рейсе"""
    flight = get_object_or_404(Flight, id=pk)
    comment = Comments.objects.filter(flight=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.flight = flight
            form.save()
            return redirect(flight_single, pk)
    else:
        form = CommentForm()
    return render(request, "flightsingle.html", {"flight": flight, "comments": comment, "form": form})