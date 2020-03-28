from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from django.http import Http404
from .models import Owner
from .models import Auto

def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def list_view(request):
    context={}

    context["dataset"] = Owner.objects.all()
    return render(request, "list_view.html", context)

class AutoList(ListView):
    model = Auto
    template_name = 'auto_view.html'