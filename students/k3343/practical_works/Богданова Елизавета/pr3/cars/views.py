from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import User, Car, Driver_license, Owning
from .forms import CarForm


def show_all_owners(request):
    owners={}
    owners["owners"] = User.objects.all()
    return render(request, 'all_owners_view.html', owners)


class CarsCreate(CreateView):
    model = Car
    fields = ['car_make','car_model','car_color','id_car']
    def as_view(request):
        autos = {}
        form = CarForm(request.POST or None)
        if form.is_valid():
            form.save()
        autos['form'] = form
        return render(request, 'create_view_cars.html', autos)


class Show_car(ListView):
    model = Car

    def as_view(request):
        cars = {}
        cars["cars"] = Car.objects.all()
        return render(request, 'cars.html', cars)