from django.shortcuts import render
from simple_django_app.models import Auto, Owner
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


from .forms import OwnerForm


class AutoView(ListView):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["autos"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Autos does not exist")
        return render(request, 'auto_list.html', context)


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def show_owners(request):
    context = {}
    try:
        context["owners"] = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


def show_thanks(request):
    return render(request, 'thanks.html')


def add_owner(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/thanks')

    return render(request, 'owner_form.html', {'form': form})



class AddAuto(CreateView):
    model = Auto
    fields = ["manufacture", "model", "color", "gov_number"]
    template_name = "auto_form.html"
