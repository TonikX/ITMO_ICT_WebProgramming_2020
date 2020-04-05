from django.shortcuts import render
from django.http import Http404
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import Owner, Ownership, Car, Certificate
# Create your views here.

def detail(request,ow_id):
    try:
        ownerr=Owner.objects.get(pk=ow_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request,'owner.html',{"owner":ownerr})

def show_owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "owners_list.html", context)

class Show_cars(ListView):
    model=Car
    template_name = 'cars_list.html'

def createowner(request):
    context = {}
    form = OwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)

class Car_create(CreateView):
    model=Car
    fields=['brand','model','color','code']
    template_name = 'create_cars.html'