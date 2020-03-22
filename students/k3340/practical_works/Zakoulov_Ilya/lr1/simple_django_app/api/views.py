from django.shortcuts import render
from simple_django_app.models import Car
from django.http import Http404


def get(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404("Car does not exist")
    return render(request, 'cars/show.html', {'car': car})
