from django.http import Http404

from django.shortcuts import render

from .models import CarOwner

# Create your views here.

def owner_data(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'car_owner': owner})