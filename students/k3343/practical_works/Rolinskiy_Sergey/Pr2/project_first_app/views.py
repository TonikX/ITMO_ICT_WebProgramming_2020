from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner, Ownership, Car, Certificate
# Create your views here.

def detail(request,ow_id):
    try:
        ownerr=Owner.objects.get(pk=ow_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request,'owner.html',{"owner":ownerr})