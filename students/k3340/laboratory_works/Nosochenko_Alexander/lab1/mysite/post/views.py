from django.shortcuts import render, get_object_or_404, redirect
from post.models import Info, Comment
from post.forms import CommentForm


def info_list(request):
    info = Info.objects.all()
    return render(request, "info/info_list.html", {"info": info})


def single_info(request, pk):
    info = get_object_or_404(Info, id=pk)
    comments = Comment.objects.filter(info=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = request.user
            form.info = info
            form.save()
            return redirect(single_info, pk)
    else:
        form = CommentForm()
    return render(request, "info/info_single.html", {"info": info,
                                                     "comments": comments,
                                                     "form": form})