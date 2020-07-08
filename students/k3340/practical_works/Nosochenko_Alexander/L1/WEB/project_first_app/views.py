from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Person
from django.http import HttpResponse
import datetime

def detail(request, poll_id):
    try:
        info = Person.objects.get(pk=poll_id)
    except Person.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_first_app/main.html', {'person': info})

def geeks_view(request):
    # fetch date and time
    now = datetime.datetime.today().strftime("Time: %H.%M.%S Date: %Y-%m-%d")
    # convert to string
    # html = " {}".format(now)
    # return response
    return HttpResponse(now)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()

    return render(request, "test.html", context)
