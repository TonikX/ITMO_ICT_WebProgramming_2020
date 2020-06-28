from django.shortcuts import render, get_object_or_404, redirect
from .models import Homework, Comments
from .forms import CommentForm


def homework_table(request):
    """Вывод всех новостей
    """
    homeworks = Homework.objects.all()
    return render(request, "homework_table.html", {"homeworks": homeworks})


def homework_single(request, pk):
    """Вывод полной статьи
    """
    homework = get_object_or_404(Homework, id=pk)
    comment = Comments.objects.filter(homework=pk)
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
    return render(request, "homework_single.html",
                  {"homework": homework,
                   "comments": comment,
                   "form": form})
