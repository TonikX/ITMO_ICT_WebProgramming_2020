from django.shortcuts import render
from django.http import Http404
from .models import Car_owner

def detail(request, owner_id):
    try:
        ao = Car_owner.objects.get(pk=owner_id)
    except Car_owner.DoesNotExist:
        raise Http404("Car_owner does not exist")
    return render(request,'owner.html',{'Car_owner':ao})
