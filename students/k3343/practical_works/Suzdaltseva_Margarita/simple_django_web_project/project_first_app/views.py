from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render
from .models import CarOwner, ExampleModel, Car
from django.views.generic.list import ListView

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

def list_view(request):
    context = {}
    context["dataset"] = ExampleModel.objects.all()
    return render(request, "list_view.html", context)

class ExampleList(ListView):
    model = ExampleModel

    def get(self, request):
        context = {}
        context["object_list"] = ExampleModel.objects.all()
        return render(request, "examplemodel_list.html", context)

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