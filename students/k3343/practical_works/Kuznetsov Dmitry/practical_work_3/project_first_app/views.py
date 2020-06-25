from django.shortcuts import render

from django.http import Http404

from .models import Owner, Car

from django.views.generic.list import ListView

from .forms import OwnerForm, CarForm



def detail(request, owner_id):

    try:

        p = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:

        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': p})


def owners_detail(request):

    context = {}

    try:

        context["owners"] = Owner.objects.all()

    except Owner.DoesNotExist:

        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


class CarsView(ListView):

    model = Car

    def get(self, request):

        context = {}

        try:

            context["cars"] = Car.objects.all()

        except Car.DoesNotExist:

            raise Http404("Car does not exist")

        return render(request, 'cars.html', context)



def add_owner(request):

    context = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():

        form.save()

    context['form'] = form

    return render(request, "add_owner.html", context)


def add_car(request):

    context = {}

    form = CarForm(request.POST or None)

    if form.is_valid():

        form.save()

    context['form'] = form

    return render(request, "add_car.html", context)