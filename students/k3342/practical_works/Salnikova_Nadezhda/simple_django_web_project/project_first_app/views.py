from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from project_first_app.models import Owner, Car, DriverLicense, Ownership


def owner_detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owner_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Owner.objects.all()

    return render(request, "owner_list.html", context)


class CarList(ListView):
    # specify the model for list view
    model = Car
