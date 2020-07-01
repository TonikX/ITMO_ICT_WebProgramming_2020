from django.shortcuts import render, get_object_or_404, redirect
from .models import Workshop, Comments
from .forms import CommentForm


def wsh_list(request):
    wsh = Workshop.objects.all()
    return render(request, "wsh/Workshops_View.html", {"workshops_data": wsh})


def workshop_single(request, pk):
    wsh = get_object_or_404(Workshop, id=pk)
    comment = Comments.objects.filter(workshop=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.workshop = wsh
            form.save()
            return redirect(workshop_single, pk)
    else:
        form = CommentForm()
    return render(request, "wsh/Workshop_single.html", {"workshop": wsh, "comments":comment, "form":form})