from django.http import Http404, HttpResponse
from django.shortcuts import render
from project_first_app.models import Owner, Car
import datetime
from django.views.generic.list import ListView


from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.
from .forms import Owner_form


def detail(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "Owner.html", {'owner': o})
    # return HttpResponse("<html><body>Имя: '{{ o.name }}', Фамилия: '{{ o.surname }}' </body></html>")


def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


def owners_list(request):
    contex = {'owners_data': Owner.objects.all()}
    return render(request, "owners.html", contex)


class CarList(ListView):
    model = Car
    template_name = 'create_cars.html'

def list_view(request):
    context={}

    context["dataset"] = Owner.objects.all()
    return render(request, "owners.html", context)

def create_owners(request):
    context = {}
    form = Owner_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owners.html", context)

class Car_create(CreateView):
    model = Car
    fields = [
        'Mark',
        'Model',
        'Color',
        'Gov_number'
    ]
    template_name = 'create_cars.html'


