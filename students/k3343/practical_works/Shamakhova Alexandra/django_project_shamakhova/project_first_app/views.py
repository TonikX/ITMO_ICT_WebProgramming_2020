from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import User as CarOwner, Car
from .forms import CarOwnerForm


def car_owner_info(request, car_owner_id):
    try:
        car_owner = CarOwner.objects.get(pk=car_owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'car_owner': car_owner})


def car_owner_list(request):
    context = {"dataset": CarOwner.objects.all()}
    return render(request, "owner_list.html", context)


class CarList(ListView):
    model = Car

    def get(self, request, **kwargs):
        context = {"object_list": Car.objects.all()}
        return render(request, "car_list.html", context)


def car_owner_form(request):
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "owner_form.html", context)


class CarForm(CreateView):
    model = Car
    fields = ['car_maker', 'car_model', 'car_colour', 'car_number']
    template_name = "car_form.html"
