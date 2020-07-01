from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import Owner, Car, DriverLicense, Ownership
from .forms import OwnerForm


def owner_detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owner_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Owner.objects.all()

    return render(request, "owner_list.html", context)


def create_owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    form = OwnerForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner_view.html", context)


class CarList(ListView):
    # specify the model for list view
    model = Car


class CarCreate(CreateView):
    # specify the model for create view
    model = Car

    # specify the fields to be displayed
    fields = ['car_number', 'brand', 'model', 'color']
    success_url = '/car_form'
