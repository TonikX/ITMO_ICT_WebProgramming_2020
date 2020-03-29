from django.shortcuts import render
from project_first_app.models import Owner, Auto
from django.http import Http404
from django.views import View


# Create your views here.
def get_owner_info(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def get_owners_info(request):
    context = {}
    try:
        context["owners"] = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)


class AutoInfoView(View):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["autos"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Auto does not exist")
 
        return render(request, 'auto.html', context)
