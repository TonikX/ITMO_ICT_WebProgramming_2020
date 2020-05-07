from django.shortcuts import render
from project_first_app.models import User as Driver, Auto
from django.http import Http404
from django.views import View
from .forms import NewDriverForm
from django.views.generic.edit import CreateView


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


def get_driver_form(request):
    form = NewDriverForm(request.POST)

    context = {}
    context["form"] = form

    if form.is_valid():
        form.save()

    return render(request, 'new_driver_form.html', context)


class GetAutoForm(CreateView):

    model = Auto
    
    fields = [
        "manufacture", 
        "model",
        "color",
        "gosnumber"
    ]
    
    template_name = "new_auto_form.html"
