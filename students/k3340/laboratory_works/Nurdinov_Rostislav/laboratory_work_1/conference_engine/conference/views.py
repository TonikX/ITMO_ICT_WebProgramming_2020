from django.shortcuts import render, redirect
from django.http import Http404
from .models import Conference, Section, Speech, Comment
from .forms import CommentForm
import datetime


def conference(request):
    confs = Conference.objects.all().reverse()[:3]
    return render(request, 'conference/base_conference.html', context={'confs': confs})


def detail(request, cid):
    try:
        conf = Conference.objects.get(pk=cid)
        comments = Comment.objects.filter(conference=conf)
        sections = Section.objects.filter(conference=conf).order_by('date_start')
        speech_dict = {}
        form = CommentForm(request.POST or None)
        form.user = request.user
        if request.method == "POST":
            if form.is_valid:
                form = form.save(commit=False)
                form.user = request.user
                form.conference = conf
                form.save()
                return redirect(detail, cid)
            else:
                print(form.errors)
        for section in sections:
            speechs = Speech.objects.filter(section=section)
            speech_dict[section] = []
            for elem in speechs:
                speech_dict[section].append([elem.speaker, elem.lecture])
    except Conference.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'conference/conf_detail.html', context={'sections': sections, 'speech': speech_dict,
                                                                   'comments': comments, 'form': form})


def about(request):
    return render(request, 'conference/about.html')


def archive(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__lt=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'conference/archive.html', context={'confs': confs})


def future_conf(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__gte=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'conference/future_conf.html', context={'confs': confs})
