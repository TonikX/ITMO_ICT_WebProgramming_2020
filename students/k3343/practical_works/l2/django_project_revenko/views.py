from django.shortcuts import render
from project_first_app.models import Owner, Car
from django.http import Http404
from django.views import View


def owner_inf(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def owners_inf(request):
    context = {}
    try:
        context["owners"] = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


class CarsView(View):
    model = Car

    def cars_inf(self, request):
        context = {}
        try:
            context["cars"] = Car.objects.all()
        except Car.DoesNotExist:
            raise Http404("Car does not exist")

        return render(request, 'car.html', context)