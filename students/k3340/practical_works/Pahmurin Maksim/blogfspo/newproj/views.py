from django.http import Http404
from django.shortcuts import render
from .models import Autoholder, Automobile, AdditionalData
from django.views.generic.list import ListView
from .forms import HolderForm
from django.views.generic.edit import CreateView


def detail(request, poll_id):
    try:
        o = Autoholder.objects.get(pk=poll_id)
        addit = AdditionalData.objects.filter(owner=o).values()
        if len(addit) == 0:
            addit = {}
        else:
            addit = addit[0]
    except Autoholder.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'poll': o, 'addit': addit})


def show_autoholders_list(request):
    context = {'dataset': Autoholder.objects.all()}
    return render(request, 'autoholders_list.html', context)


class AutoList(ListView):
    template_name = 'auto_list.html'
    model = Automobile


def holder_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = HolderForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "holder_view.html", context)


def success(request):
    return render(request, 'success.html')


class AutoForm(CreateView):
    template_name = 'auto_form.html'
    model = Automobile

    fields = ['mark', 'model_car', 'color', 'nomber']
