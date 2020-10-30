from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Car, CarOwner
from .forms import OwnerForm


def index(request):
    owners = CarOwner.objects.all()

    return render(request, 'project_first_app/index.html', context={'owners': owners})

def owner(request, id):
    try:
        car_owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404('User Does not exist !')
    return render(request, 'project_first_app/car_owner.html', context={'owners': car_owner})

# Practice 2
def list_view(request):
    context = {}

    context["owners"] = CarOwner.objects.all()

    return render(request, "project_first_app/list_view.html", context=context)


class CarsView(ListView):
    model = Car
    template_name = "project_first_app/car_view.html"
    context_object_name = 'cars'


def create_owner(request):
    context ={}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "project_first_app/create_owner.html", context)

class CreateCar(CreateView):
    model = Car
    context_object_name = 'form'
    fields = [
        'car_brand',
        'car_model',
        'car_color',
        'state_number'
    ]
    template_name = "project_first_app/car_create.html"