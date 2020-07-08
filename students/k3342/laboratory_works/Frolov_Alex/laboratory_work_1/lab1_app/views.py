from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .forms import AddComment
from .models import Conference, Comment


def index(request):
    return render(request, 'index.html')


class ConferenceView(ListView):
    model = Conference

    def get(self, request):
        context = {}

        try:
            context["conferences"] = Conference.objects.all()
        except Conference.DoesNotExist:
            raise Http404("Conference does not exist")

        return render(request, 'all_conferences.html', context)


def about_conf(request, conf_id):
    global user_id
    try:
        conference = Conference.objects.get(pk=conf_id)
    except Conference.DoesNotExist:
        raise Http404("Conference does not exist")

    try:
        comments = Comment.objects.filter(conference_name=conf_id).all()
    except Comment.DoesNotExist:
        pass

    if request.POST.get('user_id'):
        user_id = int(request.POST.get('user_id'))

    form = AddComment(request.POST)

    if form.is_valid():

        conference_form = form.save(commit=False)
        conference_form.post = form
        conference_form.conf_id = conf_id
        conference_form.participant_id = user_id
        conference_form.save()

        return HttpResponseRedirect('/conferences/{}/'.format(conf_id))

    return render(request, 'conference_info.html', {'conference': conference, 'comments': comments, 'form': form})
# Create your views here.
