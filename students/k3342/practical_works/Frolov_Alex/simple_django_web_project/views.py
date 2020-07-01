from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from .forms import OwnerForm, AvtoForm
from .models import User, Avto


def detail(request, username):
    try:
        owner = User.objects.get(pk=username)
    except User.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owners_detail(request):
    context = {}
    try:
        context["owners"] = User.objects.all()
    except User.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owners.html', context)


class CarsView(ListView):
    model = Avto

    def get(self, request):
        context = {}

        try:
            context["avtos"] = Avto.objects.all()
        except Avto.DoesNotExist:
            raise Http404("Car does not exist")

        return render(request, 'car.html', context)


def add_owner(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)


def add_avto(request):
    context = {}

    form = AvtoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_car.html", context)
