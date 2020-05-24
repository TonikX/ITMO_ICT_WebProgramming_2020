from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner, Car
from django.views.generic.list import ListView
from project_first_app.forms import OwnersForm
from django.views.generic.edit import CreateView

def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk = owner_id)
    except Owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'detail.html', {'owner': owner})

def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


# 2.1
def show_owners(request):
    owners = {"dataset": Owner.objects.all()}
    return render(request, 'owners.html', owners)

# 2.2
class CarsList(ListView):
    model = Car

def owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()
    return render(request, "owners.html", context)

def create_view(request):
    context = {}

    form = OwnersForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarCreate(CreateView):
    model = Car
    fields = ["car_number", "brand_name", "model_name", "colour"]