from django.shortcuts import render
from .forms import AddComment
from .models import Conference, Comment
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView



def index(request):
    return render(request, 'index.html')


def show_conferences(request):
    conferences = {}
    conferences["conferences"] = Conference.objects.all()
    return render(request, 'all_conferences.html', conferences)


def show_comments(request):
    comments = {}
    comments["comments"] = Comment.objects.all()
    return render(request, 'all_comments.html', comments)



class Add_Comment(CreateView):
    model = Comment
    fields = [
            "conference",
            "type_of_comment",
            "text",
        ]
    def as_view(request):
        comments = {}
        form = AddComment(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.participant = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('all_comments'))
        comments['form'] = form
        return render(request, 'add_comment.html', comments)
# Create your views here.
