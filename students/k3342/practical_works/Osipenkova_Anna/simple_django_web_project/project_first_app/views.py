from django.shortcuts import render
from django.http import Http404
from project_first_app.models import *
from django.http import Http404
from django.views import View
from django.views.generic.edit import CreateView
from .forms import NewOwnerForm


def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


class AutoView(View):
    model = Auto


def get_auto(request):
    context = {}
    try:
        context["auto"] = Auto.objects.all()
    except Auto.DoesNotExist:
        raise Http404("Auto does not exist")

    return render(request, 'auto.html', context)


def get_owners(request):
    context = {}
    try:
        context["owners"] = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


def new_owner(request):
    context = {}
    form = NewOwnerForm(request.POST)
    context['form'] = form

    if form.is_valid():
        form.save()

    return render(request, 'new_owner.html', context)


class NewAuto(CreateView):
    model = Auto
    fields = ["brand_name", "model_name", "colour", "car_number", "car_owner"]
    template_name = "new_auto.html"
