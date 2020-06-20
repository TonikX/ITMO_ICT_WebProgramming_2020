from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from project_first_app.models import Owner, Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
import datetime

from .models import Owner
from .forms import OwnersForm

def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def geeks_view(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now) # convert to string
    return HttpResponse(html)

def owners_list(request):
    context = {'owners_data': Owner.objects.all()}
    return render(request, "owners.html", context)

class CarList(ListView):
    model = Car

def create_view(request):
    context = {}
    form = OwnersForm(
        request.POST or None)  # создаем экземпляр формы, отсылаем в него данные из формы (из полей в браузере)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/add_owners/')
    context['form'] = form
    return render(request, "create_owner.html", context)


class CarCreate(CreateView):
    model = Car
    fields = ['name', 'model', 'colour', 'gov_number']
    success_url = '/add_cars/'
