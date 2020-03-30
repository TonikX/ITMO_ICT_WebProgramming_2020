from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from .models import Auto_owner, Automobile, Driver_license, Owning


def detail(request,owner_id):
    try:
        auto_owner = Auto_owner.objects.get(pk=owner_id)
    except Auto_owner.DoesNotExist:
        raise Http404("Auto_owner does not exist")
    return render(request,'auto_owner.html',{'auto_owner':auto_owner})


def show_all_owners(request):
    owners={}
    owners["owners"] = Auto_owner.objects.all()
    return render(request, 'all_owners_view.html', owners)


class Show_auto(ListView):
    model = Automobile

    def as_view(request):
        autos = {}
        autos["autos"] = Automobile.objects.all()
        return render(request, 'cars.html', autos)

# Create your views here.