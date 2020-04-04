from django.http import Http404, HttpResponse
from django.shortcuts import render
from project_first_app.models import Owner, Car
import datetime
from django.views.generic.list import ListView


from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.
from django.http import Http404
from .models import Owner
from .models import Car
from .forms import OwnerForm



def detail(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "Owner.html", {'owner': o})
    # return HttpResponse("<html><body>Имя: '{{ o.name }}', Фамилия: '{{ o.surname }}' </body></html>")


def post_list(request):
    return HttpResponse('<h1>Hello!</h1>')


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
    template_name = 'form_cars.html'
#----------------------------

def list_view(request):
    context={}

    context["dataset"] = Owner.objects.all()
    return render(request, "owners.html", context)

def create_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "form_owners.html", context)

class CarCreate(CreateView):
    model = Car
    fields = [
        'mark',
        'model',
        'color',
        'number'
    ]
    template_name = 'form_cars.html'


