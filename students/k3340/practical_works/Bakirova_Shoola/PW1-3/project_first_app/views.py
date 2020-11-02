from django.shortcuts import render
from .models import *
from django.views import View
from .forms import *
from django.http import Http404
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


User = get_user_model()


def carowner(request, owner_id):
    try:
        owner = User.objects.get(pk=owner_id)
    except User.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'owner.html', {'owner': owner})


class CarView(View):
    model = Car

    def get(self, request):
        context = {}
        try:
            context["cars"] = Car.objects.all()
        except Car.DoesNotExist:
            raise Http404("Car does not exist")

        return render(request, 'car.html', context)


def owner_list(request):
    context = {}
    try:
        context["owners"] = User.objects.all()
    except User.DoesNotExist:
        raise Http404("User does not exist")

    return render(request, 'owners.html', context)


def new_owner(request):

    context = {}
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'owner_form.html', context)


class NewCar(CreateView):
    model = Car
    fields = ["mark", "model", "color", "state_num"]
    template_name = "car_form.html"