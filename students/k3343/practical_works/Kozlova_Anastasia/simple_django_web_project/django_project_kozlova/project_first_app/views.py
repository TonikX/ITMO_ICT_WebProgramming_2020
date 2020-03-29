from django.shortcuts import render
from project_first_app.models import Owner, Auto
from django.http import Http404
from django.views import View


# Create your views here.
def owner_info(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


class AboutAutoView(View):
    model = Auto
    def get(self, request):
        context = {}
        try:
            context["auto"] = Auto.objects.all()
        except Auto.DoesNotExist:
            raise Http404("Auto does not exist")
 
        return render(request, 'auto.html', context)


def owners_info(request):
    context = {}
    try:
        context["owners"] = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owners.html', context)
