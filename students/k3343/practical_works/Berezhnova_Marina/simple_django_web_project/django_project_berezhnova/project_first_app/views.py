from django.shortcuts import render
from project_first_app.models import Driver
from django.http import Http404


# Create your views here.
def get_driver(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'driver.html', {'driver': driver})
