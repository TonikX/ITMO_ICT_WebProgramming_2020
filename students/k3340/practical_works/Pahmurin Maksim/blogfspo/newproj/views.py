from django.http import Http404
from django.shortcuts import render
from .models import Autoholder


def detail(request, poll_id):
    try:
        o = Autoholder.objects.get(pk=poll_id)
        print(o)
    except Autoholder.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'poll': o})