from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Flight, AviaCompany, Comment
from .forms import AddCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect


def show_flights(request):
    """Вывод всех авирейсов"""
    flights = Flight.objects.all()
    return render(request, 'all_flights.html', {"flights": flights})


def show_aviacompanies(request):
    """Вывод всех авирейсов"""
    avias = AviaCompany.objects.all()
    return render(request, 'avia_companies.html', {"avias": avias})


def show_flight_single(request, pk):
    """Вывод полной информации об авирейсе"""
    flight = get_object_or_404(Flight, id=pk)
    comment = Comment.objects.filter(flight=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.flight = flight
            form.save()
            return redirect(show_flight_single, pk)
    else:
        form = AddCommentForm()
    return render(request, "single_flight.html",
                  {
                      "flight": flight,
                      "comments": comment,
                      "form": form,
                  })

