from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner, Auto
from django.views.generic.list import ListView
from project_first_app.forms import OwnersForm
from django.views.generic.edit import CreateView
# Create your views here.


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def show_all_owners(request):
    owners = {"dataset": Owner.objects.all()}
    return render(request, 'all_owners.html', owners)


class CarList(ListView):
    model = Auto


def create_view(request):
    context = {}

    form = OwnersForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class AutoCreate(CreateView):
    model = Auto

    fields = ["car_number", "brand_name", "model_name", "colour"]
