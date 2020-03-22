from django.shortcuts import render

# Create your views here.
from django.http import Http404

from project_first_app.models import CarOwner

def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk = owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': owner})