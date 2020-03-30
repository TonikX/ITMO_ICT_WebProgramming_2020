from django.shortcuts import render
from project_first_app.models import Owner, Car
from django.http import Http404
from django.views import View


def owner_info(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def owners_info(request):
    context = {}
    try:
        context["owners"] = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


class CarsView(View):
    model = Car

    def cars_info(self, request):
        context = {}
        try:
            context["cars"] = Car.objects.all()
        except Car.DoesNotExist:
            raise Http404("Car does not exist")

        return render(request, 'car.html', context)