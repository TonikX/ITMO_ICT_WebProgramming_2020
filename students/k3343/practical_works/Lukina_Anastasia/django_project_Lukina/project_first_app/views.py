from django.shortcuts import render

# Create your views here.
from django.http import Http404

from project_first_app.models import CarOwner
from project_first_app.models import GeeksModel
from project_first_app.models import Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import GeeksForm
from .forms import CarOwnerForm


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': owner})


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)


def all_owners_output(request):
    context = {}
    context["dataset"] = CarOwner.objects.all()
    return render(request, "all_owners_output.html", context)


class GeeksList(ListView):
    model = GeeksModel


class CarsList(ListView):
    model = Car


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


def add_car_owners(request):
    context = {}
    form = CarOwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['new_form'] = form
    return render(request, "add_car_owners.html", context)


class GeeksCreate(CreateView):
    # specify the model for create view
    model = GeeksModel

    # specify the fields to be displayed

    fields = ['title', 'description']
    success_url = '/geekcreate/'


class add_cars(CreateView):
    model = Car
    fields = ['car_brand', 'model', 'color', 'state_number']
    success_url = '/add_cars/'

