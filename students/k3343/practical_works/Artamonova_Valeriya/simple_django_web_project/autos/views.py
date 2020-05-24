from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import User, Automobile, DriverLicense, Owning
from .forms import AutomobileForm


def detail(request,username):
    try:
        auto_owner = User.objects.get(pk=username)
    except User.DoesNotExist:
        raise Http404("Auto_owner does not exist")
    return render(request,'auto_owner.html',{'auto_owner':auto_owner})


def show_all_owners(request):
    owners={}
    owners["owners"] = User.objects.all()
    return render(request, 'all_owners_view.html', owners)


class ShowAutoView(ListView):
    model = Automobile

    def as_view(request):
        autos = {}
        autos["autos"] = Automobile.objects.all()
        return render(request, 'cars.html', autos)



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
