from django.shortcuts import render

# Create your views here.
from django.http import Http404

from project_first_app.models import CarOwner
from project_first_app.models import GeeksModel
from project_first_app.models import Car
from django.views.generic.list import ListView


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk = owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': owner})

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)

def all_owners_output(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "all_owners_output.html", context)

class GeeksList(ListView):
    model = GeeksModel

class CarsList(ListView):
    model = Car
