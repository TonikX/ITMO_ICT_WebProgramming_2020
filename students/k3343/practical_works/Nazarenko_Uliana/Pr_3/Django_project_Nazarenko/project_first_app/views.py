from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render
from .models import CarOwner, Info, Car
from django.views.generic.list import ListView
from .forms import AddOwner
from django.views.generic.edit import CreateView

def owner_info(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner doesn't exist")
    return render(request, 'owner.html', {'owner': owner})

def time_info(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)


class InfoList(ListView):
    model = Info

    def get(self, request):
        context = {}
        context["object_list"] = Info.objects.all()
        return render(request, "info.html", context)

def owner_list(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "owner_list.html", context)

class CarList(ListView):
    model = Car

    def get(self, request):
        context = {}
        context["object_list"] = Car.objects.all()
        return render(request, "car_list.html", context)

def add_owner(request):
    context = {}

    form = AddOwner(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)

class AddCar(CreateView):
    model = Car
    fields = ["mark", "model", "color", "number"]
    template_name = "add_car.html"
