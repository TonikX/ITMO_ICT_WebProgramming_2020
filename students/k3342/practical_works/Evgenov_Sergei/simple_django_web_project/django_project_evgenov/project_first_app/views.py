from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.contrib.auth import get_user_model
from project_first_app.models import Car
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


User = get_user_model()


def carowner(request, carowner_id):
    try:
        p = User.objects.get(pk=carowner_id)
    except User.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'carowner.html', {'carowner': p})


def list_view(request):
    context = {"dataset": User.objects.all()}
    return render(request, 'list_view.html', context)


class CarList(ListView):

    model = Car


class CarCreate(CreateView):

    model = Car
    success_url = 'success'

    fields = [
        "producer",
        "model",
        "color",
        "state_num"
    ]


def success(request):
    return render(request, "success.html")
