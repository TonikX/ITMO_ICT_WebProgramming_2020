from django.shortcuts import render
from project_first_app.models import Driver, Auto
from django.http import Http404
from django.views import View


# Create your views here.
def get_driver(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'driver.html', {'driver': driver})


class CarView(View):
    model = Auto
    def get(self, request):
        context = {}

        try:
            context["cars"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Car does not exist")
 
        return render(request, 'car.html', context)


def get_drivers(request):
    context = {}
    try:
        context["drivers"] = Driver.objects.all()
    except Driver.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'driver.html', context)
