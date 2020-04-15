from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner, Car
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
import datetime

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
    contex = {'owners_data': Owner.objects.all()}
    return render(request, "owners.html", contex)

class CarList(ListView):
    model = Car