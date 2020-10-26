from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from .  models import Owner
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . models import Auto
from . forms import OwnerForm


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def list_view(request):
    context={}
    context["dataset"] = Owner.objects.all()
    return render(request, "list_view.html", context)


class AutoList(ListView):
    model = Auto
    template_name = 'auto_view.html'


def create_view(request):
    context ={}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class AutoCreate(CreateView):
    model = Auto
    fields = [
        'mark',
        'model',
        'color',
        'Number'
    ]
    template_name = 'auto_form.html'