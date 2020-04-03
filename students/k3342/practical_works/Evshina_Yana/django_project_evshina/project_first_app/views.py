from django.shortcuts import render
from django.http import Http404
from project_first_app.models import Owner


def detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'project_first_app/owner.html', {'owner': p})
