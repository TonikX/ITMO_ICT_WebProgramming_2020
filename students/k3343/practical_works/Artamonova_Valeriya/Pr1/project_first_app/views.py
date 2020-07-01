from django.shortcuts import render
from django.http import Http404
from .models import Auto_owner, Automobile, Driver_license, Owning


def detail(request,owner_id):
    try:
        auto_owner = Auto_owner.objects.get(pk=owner_id)
    except Auto_owner.DoesNotExist:
        raise Http404("Auto_owner does not exist")
    return render(request,'auto_owner.html',{'auto_owner':auto_owner})

# Create your views here.