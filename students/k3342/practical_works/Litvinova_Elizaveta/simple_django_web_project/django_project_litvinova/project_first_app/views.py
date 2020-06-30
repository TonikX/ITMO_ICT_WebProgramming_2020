from django.shortcuts import render
from .models import *
from django.http import Http404
from django.views import View

# Create your views here.
def show_owner(request, owner_id):
    try:
        owner = AutoOwner.objects.get(pk=owner_id)
    except AutoOwner.DoesNotExist:
        raise Http404("AutoOwner does not exist")

    return render(request, 'owner.html', {'owner': owner})


class AutoView(View):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["autos"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Auto does not exist")
 
        return render(request, 'auto.html', context)
