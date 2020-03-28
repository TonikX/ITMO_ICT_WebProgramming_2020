from django.shortcuts import render
from simple_django_app.models import Auto, Owner
from django.http import Http404
from django.views.generic.list import ListView


class AutoView(ListView):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["autos"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Autos does not exist")
        return render(request, 'auto_list.html', context)


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})

