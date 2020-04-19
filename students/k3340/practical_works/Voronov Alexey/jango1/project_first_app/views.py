from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Person, Vehicle
from django.views.generic.list import ListView
from .forms import PersonForm

def detail(request, poll_id):
    print(poll_id)
    try: #метод try-except - обработчик исключений
        p = Person.objects.get(pk=poll_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
    except Person.DoesNotExist:
        raise Http404("Person does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'project_first_app/main.html', {'person': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"

def persons(request):
    context = {}

    try:
        context["persons"] = Person.objects.all()
    except:
        raise Http404("Pesrons does not exist")

    return render(request, 'project_first_app/persons.html', context)

class Vehicles(ListView):

    def get(self, request):
        context = {}

        try:
            context["vehicles"] = Vehicle.objects.all()
        except Vehicle.DoesNotExist:
            raise Http404("Vehicles does not exist")
        return render(request, 'project_first_app/vehicles.html', context)

def addPerson(request):
    form = PersonForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'project_first_app/pesron_form.html', {'form': form})