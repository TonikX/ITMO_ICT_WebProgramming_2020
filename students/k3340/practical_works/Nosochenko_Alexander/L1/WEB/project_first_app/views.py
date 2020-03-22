from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Person

def detail(request, poll_id):
    try:
        info = Person.objects.get(pk=poll_id)
    except Person.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_first_app/main.html', {'person': info})
