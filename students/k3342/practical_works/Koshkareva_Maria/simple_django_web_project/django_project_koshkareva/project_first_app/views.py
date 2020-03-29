from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import Http404
from .models import Owner, Ownership, Driver_license, Car


def Owner_info(request, owner_id):
    try:
        the_owner = Owner.objects.get(pk=owner_id)
        license = Driver_license.objects.get(driver=the_owner)
        owns = Ownership.objects.filter(owner=the_owner)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "project_first_app/owner_info.html",
                                            {"owner":the_owner,
                                             "owns":owns,
                                             "license":license})

def Owners_list(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "project_first_app/owners_list.html", context)

class Cars_list(ListView):
    model = Car