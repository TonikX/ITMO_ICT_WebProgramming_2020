from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.forms import NewOwnerForm
from project_first_app.models import Owner, Car


def owner_info(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})

def owner_list(request):
    context = {'dataset': Owner.objects.all()}
    return render(request, "owner_list.html", context)

class CarList(ListView):
    model = Car

def new_owner(request):
    form = NewOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "new_owner.html", context)

class NewCar(CreateView):
    model = Car
    fields = ['name', 'type', 'colour', 'number']
    template_name = "project_first_app/new_car.html"