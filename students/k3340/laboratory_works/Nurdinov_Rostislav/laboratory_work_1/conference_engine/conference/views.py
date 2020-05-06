from django.shortcuts import render
from django.http import Http404
from .models import Conference, Section, Speech
import datetime


def conference(request):
    confs = Conference.objects.all().reverse()[:3]
    return render(request, 'conference/base_conference.html', context={'confs': confs})


def detail(request, cid):
    try:
        conf = Conference.objects.get(pk=cid)
        sections = Section.objects.filter(conference=conf).order_by('date_start')
        speech_dict = {}
        print(sections)
        for section in sections:
            speechs = Speech.objects.filter(section=section)
            speech_dict[section] = []
            for elem in speechs:
                speech_dict[section].append([elem.speaker, elem.lecture])
        print(speech_dict)
    except Conference.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'conference/conf_detail.html', context={'sections': sections, 'speech': speech_dict})


def about(request):
    return render(request, 'conference/about.html')


def archive(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__lt=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'conference/archive.html', context={'confs': confs})


def future_conf(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__gte=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'conference/future_conf.html', context={'confs': confs})
