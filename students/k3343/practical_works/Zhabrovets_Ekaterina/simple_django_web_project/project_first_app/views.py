from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Owner, Car
import datetime
from django.views.generic.list import ListView
from .forms import OwnersForm
from django.views.generic.edit import CreateView


def detail(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "Owner.html", {'owner': o})
    # return HttpResponse("<html><body>Имя: '{{ o.first_name }}', Фамилия: '{{ o.last_name }}' </body></html>")


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
    return render(request, "Owners_View.html", contex)


class CarList(ListView):
    model = Car


def create_owner(request):
    contex = {}
    form_owner = OwnersForm(request.POST or None)

    if form_owner.is_valid():
        form_owner.save()
        return HttpResponseRedirect('/all_owners/')  # редирект на страницу с представлением всех пользователей
    contex['form_owner'] = form_owner
    return render(request, "Create_Owner.html", contex)


class CreateCar(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    success_url = '/all_cars/'
