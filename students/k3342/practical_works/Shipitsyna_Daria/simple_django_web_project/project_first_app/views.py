from django.shortcuts import render
from django.http import Http404
from .models import Car
from .models import Owner
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnerForm

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
    success_url = '/owner_list'


def create_owner(request):
    context = {}

    form = OwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_form.html", context)


class CarCreate(CreateView):
    model = Car
    fields = ['mark', 'model', 'colour', 'gov_number']
    success_url = '/car_list'
