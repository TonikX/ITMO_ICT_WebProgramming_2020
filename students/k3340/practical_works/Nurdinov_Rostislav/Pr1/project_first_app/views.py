from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView
from project_first_app.models import Owner, Auto
from .forms import OwnerForm
from django.views.generic.list import ListView


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def show_list_owners(request):
    context = {'dataset': Owner.objects.all()}
    return render(request, 'list_owners.html', context)


def owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_view.html", context)


def success(request):
    return render(request, 'success.html')


class ShowAuto(ListView):
    template_name = 'auto_list.html'
    model = Auto


class AutoForm(CreateView):
    template_name = 'auto_form.html'
    model = Auto

    fields = ['mark', 'model', 'color', 'gos_number']
