from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import AutoOwner, Automobile, DriverLicense, Owning
from .forms import AutoOwnerForm, AutomobileForm


def detail(request,owner_id):
    try:
        auto_owner = AutoOwner.objects.get(pk=owner_id)
    except AutoOwner.DoesNotExist:
        raise Http404("Auto_owner does not exist")
    return render(request,'auto_owner.html',{'auto_owner':auto_owner})


def show_all_owners(request):
    owners={}
    owners["owners"] = AutoOwner.objects.all()
    return render(request, 'all_owners_view.html', owners)


class ShowAutoView(ListView):
    model = Automobile

    def as_view(request):
        autos = {}
        autos["autos"] = Automobile.objects.all()
        return render(request, 'cars.html', autos)


def create_view_owners(request):
    context = {}
    form = AutoOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render (request,"create_view_owners.html", context)


class AutomobilesCreateView(CreateView):
    model = Automobile
    fields = ['car_make','car_model','car_color','id_car']
    def as_view(request):
        autos = {}
        form = AutomobileForm(request.POST or None)
        if form.is_valid():
            form.save()
        autos['form'] = form
        return render(request, 'create_view_cars.html', autos)
# Create your views here.
