from django.shortcuts import render
from simple_django_app.models import Auto, Owner
from django.http import Http404


def show_auto(request, auto_id):
    try:
        auto = Auto.objects.get(pk=auto_id)
    except Auto.DoesNotExist:
        raise Http404("Auto does not exist")

    return render(request, 'auto.html', {'auto': auto})


def show_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})

