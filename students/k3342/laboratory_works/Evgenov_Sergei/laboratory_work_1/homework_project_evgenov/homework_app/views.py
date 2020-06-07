from django.shortcuts import render

# Create your views here.

from django.http import Http404
from homework_app.models import Homework
from django.views.generic.list import ListView

def homework(request, homework_id):
    try:
        p = Homework.objects.get(pk=homework_id)
    except Homework.DoesNotExist:
        raise Http404("Homework does not exist")
    return render(request, 'homework.html', {'homework': p})

class HomeworkList(ListView):

    model = Homework