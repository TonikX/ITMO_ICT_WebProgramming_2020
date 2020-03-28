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


class AutoInfoView(View):
    def get(self, request, auto_id):
        try:
            auto = Auto.objects.get(pk=auto_id)
        except Auto.DoesNotExist:
            raise Http404("Auto does not exist")
 
        return render(request, 'auto.html', {'auto': auto})
