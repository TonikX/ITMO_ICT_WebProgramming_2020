from django.shortcuts import render
from .models import *
from django.views import View
from .forms import *
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.
def show_owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
    except AutoOwner.DoesNotExist:
        raise Http404("AutoOwner does not exist")

    return render(request, 'owner.html', {'owner': owner})


class AutoView(View):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["autos"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Auto does not exist")
 
        return render(request, 'auto.html', context)


def onwer_list(request):
    context = {}
    try:
        context["owners"] = AutoOwner.objects.all()
    except AutoOwner.DoesNotExist:
        raise Http404("AutoOwner does not exist")

    return render(request, 'owners.html', context)


def new_owner(request):
    form = AutoOwnerForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/owner/all')

    return render(request, 'owner_form.html', {'form': form})


class NewAuto(CreateView):
    model = Auto
    fields = ["manufacture", "model", "color", "gov_number"]
    template_name = "auto_form.html"
