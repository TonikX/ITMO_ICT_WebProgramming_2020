from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import Car, Owner


def owner(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'zimarinapp/detail.html', {'owner': p})


def cars(request):
    try:
        p = Car.objects.all()
    except Car.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'zimarinapp/cars.html', {'cars': p})
