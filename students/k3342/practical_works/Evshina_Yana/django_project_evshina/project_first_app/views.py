from django.shortcuts import render

from django.http import Http404

from project_first_app.models import Owner
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnerForm
from .models import Car


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owner_list(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "owner_list.html", context)


class CarList(ListView):
    model = Car


def add_owners(request):
    context ={}
    form = OwnerForm(request.POST or None)
    #создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():
        #Проверка формы на корректность (валидация)
        form.save()
    context['form']= form
    return render(request, "add_owners.html", context)


class add_cars(CreateView):
    model = Car
    fields = ['name', 'type', 'colour', 'number']
    success_url = '/add_cars/'










