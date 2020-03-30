from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from .models import Car_owner, Car, Driver_license, Owning

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


class Show_car(ListView):
    model = Car

    def as_view(request):
        cars = {}
        cars["cars"] = Car.objects.all()
        return render(request, 'cars.html', cars)