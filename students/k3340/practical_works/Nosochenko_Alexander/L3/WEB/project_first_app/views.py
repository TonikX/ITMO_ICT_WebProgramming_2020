from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Person, Vehicle
from django.http import HttpResponse
import datetime
from django.views.generic.list import ListView
from .forms import PersonForm
from django.views.generic.edit import CreateView


from .forms import PersonForm

def detail(request, poll_id):
    try:
        info = Person.objects.get(pk=poll_id)
    except Person.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_first_app/main.html', {'person': info})

def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.today().strftime("Time: %H.%M.%S Date: %Y-%m-%d")
    # convert to string
    # html = " {}".format(now)
    # return response
    return HttpResponse(now)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()

    return render(request, "persons.html", context)


class VehiclesList(ListView):
    # specify the model for list view
    model = Vehicle


def create_person_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PersonForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():  # Проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "personform_view.html", context)


class VehicleCreate(CreateView):
    # specify the model for create view
    model = Vehicle

    # specify the fields to be displayed

    fields = ['manufacturer', 'model', 'vehicle_number', 'color']

