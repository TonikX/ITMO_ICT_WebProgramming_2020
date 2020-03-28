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
    def get(self, request, auto_id):
        try:
            car = Auto.objects.get(pk=auto_id)
        except Auto.DoesNotExist:
            raise Http404("Car does not exist")
 
        return render(request, 'car.html', {'car': car})
