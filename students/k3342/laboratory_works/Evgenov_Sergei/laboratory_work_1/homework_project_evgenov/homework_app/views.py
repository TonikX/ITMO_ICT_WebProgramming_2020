from django.shortcuts import render, redirect

# Create your views here.

from django.http import Http404
from homework_app.models import Homework, Comment
from django.views.generic.list import ListView
from homework_app.forms import CommentForm

def homework(request, homework_id):
    p = Homework.objects.get(pk=homework_id)
    context = {"dataset": Comment.objects.filter(homework=p), "homework": p}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.homework = p
            form.save()
        return redirect("homework_single", homework_id)
    else:
        form = CommentForm()
    context["form"] = form
    return render(request, 'homework.html', context)

class HomeworkList(ListView):

    model = Homework