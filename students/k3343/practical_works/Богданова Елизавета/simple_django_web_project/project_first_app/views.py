from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Car_owner, Car, Driver_license, Owning
from .forms import Car_ownerForm, CarForm

def detail(request, owner_id):
    try:
        ao = Car_owner.objects.get(pk=owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Car_owner does not exist")
    return render(request,'owner.html',{'Car_owner':ao})

def show_all_owners(request):
    owners={}
    owners["owners"] = Car_owner.objects.all()
    return render(request, 'all_owners_view.html', owners)

def create_view_owners(request):
    context = {}
    form = Car_ownerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render (request,"create_view_owners.html", context)


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