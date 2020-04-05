from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import Http404
from .models import Owner, Ownership, Driver_license, Car
from .forms import OwnerForm


# PrW_1
def owner_info(request, owner_id):
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


# PrW_2
#   Task 2
def owners_list(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "project_first_app/owners_list.html", context)


class CarsList(ListView):
    model = Car


#   Task 3
def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request,"project_first_app/create_owner.html", context)


class CreateCar(CreateView):
    model = Car
    fields = ["make","model","colour","reg_plate"]
    success_url = "/car_form/"

