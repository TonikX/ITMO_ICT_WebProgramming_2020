from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import  *
from .forms import CommentForm

def hw_list(request):
    hw = Homework.objects.all()
    return render(request, 'hw/index.html', context={'names': hw})

def comments_list(request):
    comments = Comment.objects.filter(moderation=True)
    return render(request, 'hw/comments.html', context={'comments': reversed(comments)})

def hw_detail(request, pk):
    detailed_hw = get_object_or_404(Homework, pk=pk)
    comment = Comment.objects.filter(homework=pk, moderation=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.commentator = request.user
            new_comment.homework = detailed_hw
            new_comment.save()
            return redirect(detailed_hw, pk=pk)
    else:
        form = CommentForm()
    context = {
        'detailed_hw': detailed_hw,
        'comments': reversed(comment),
        'form': form
    }
    return render(request, 'hw/hw_detail.html', context=context)
