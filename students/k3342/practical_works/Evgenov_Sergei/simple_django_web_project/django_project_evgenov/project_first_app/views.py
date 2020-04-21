from django.shortcuts import render

# Create your views here.

from django.http import Http404
from project_first_app.models import CarOwner
from project_first_app.models import Car
from django.views.generic.list import ListView
from project_first_app.forms import OwnerForm
from django.views.generic.edit import CreateView


def carowner(request, carowner_id):
    try:
        p = CarOwner.objects.get(pk=carowner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'carowner.html', {'carowner': p})


def list_view(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, 'list_view.html', context)


class CarList(ListView):

    model = Car


def create_view(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarCreate(CreateView):

    model = Car
    success_url = 'success'

    fields = [
        "producer",
        "model",
        "color",
        "state_num"
    ]


def success(request):
    return render(request, "success.html")
