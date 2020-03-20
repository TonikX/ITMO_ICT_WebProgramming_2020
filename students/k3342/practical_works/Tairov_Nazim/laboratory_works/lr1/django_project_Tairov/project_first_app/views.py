from django.http import Http404
from django.shortcuts import render

from .models import CarOwner


def index(request):
    owners = CarOwner.objects.all()

    return render(request, 'project_first_app/index.html', context={'owners': owners})

def owner(request, id):
    try:
        car_owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404('User Does not exist !')
    return render(request, 'project_first_app/car_owner.html', context={'owners': car_owner})
