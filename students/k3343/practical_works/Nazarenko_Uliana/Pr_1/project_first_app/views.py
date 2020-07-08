from django.http import Http404
from django.shortcuts import render
from .models import Car_owner

def detail(request, Car_owner_id):
    try:
        p = Car_owner.objects.get(pk=Car_owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'Car_owner': p})
