from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render
from .models import CarOwner, Car
from django.views.generic.list import ListView
from .forms import OwnerForm
from django.views.generic.edit import CreateView

def owner_info(request, carowner_id):
    try:
        owner = CarOwner.objects.get(pk=carowner_id)
    except CarOwner.DoesNotExist:
        raise Http404("car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def time_info(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)

def ownerlist(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "ownerlist.html", context)

class CarList(ListView):
    model = Car

    def get(self, request):
        context = {}
        context["object_list"] = Car.objects.all()
        return render(request, "carlist.html", context)

def create_owner(request):
    context = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)

class CarCreate(CreateView):
    model = Car
    fields = ["trademark", "model", "color", "number"]
    template_name = "car_form.html"

