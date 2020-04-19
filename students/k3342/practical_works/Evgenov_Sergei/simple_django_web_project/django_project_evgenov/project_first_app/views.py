from django.shortcuts import render

# Create your views here.

from django.http import Http404
from project_first_app.models import CarOwner


def carowner(request, carowner_id):
    try:
        p = CarOwner.objects.get(pk=carowner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'carowner.html', {'carowner': p})
