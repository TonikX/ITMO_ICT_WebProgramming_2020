from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render
from .models import CarOwner

def owner_info(request, carowner_id):
    try:
        owner = CarOwner.objects.get(pk=carowner_id)
    except CarOwner.DoesNotExist:
        raise Http404("car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})