from django.shortcuts import render, get_object_or_404, redirect
from .models import Homeworks, Comments
from .forms import CommentForm
from datetime import datetime, timedelta


def homework_list(request):
    """Вывод всех домашних заданий
    """
    homeworks = Homeworks.objects.all()
    return render(request, "homeworks/homework_list.html", {"homeworks": homeworks})


def homework_single(request, pk):
    """Вывод полного дз
    """
    homework: object = get_object_or_404(Homeworks, id=pk)
    comments = Comments.objects.filter(homework=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.homework = homework
            form.save()
            return redirect(homework_single, pk)
    else:
        form = CommentForm()
    return render(request, "homeworks/homework_single.html",
                  {"homework": homework,
                   "comments": comments,
                   "form": form})


