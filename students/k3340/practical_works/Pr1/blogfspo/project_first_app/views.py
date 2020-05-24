from django.http import Http404
from django.shortcuts import render
from .models import Auto

def detail(request, poll_id):
    try:
        o = Auto.objects.get(pk=poll_id)
        print(o)
    except Auto.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'poll': o})