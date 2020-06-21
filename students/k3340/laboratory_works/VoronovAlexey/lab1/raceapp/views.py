from django.shortcuts import render, redirect
from django.http import Http404
from .models import Result, Comment
from raceapp import forms

# Create your views here.

def results(request):
    context = {}
    try:
        context["results"] = Result.objects.all
    except:
        raise Http404("results does not exist")
    return render(request, 'results.html', context)

def result(request, id):
    context = {}

    result = Result.objects.get(id=id)

    comments = Comment.objects.filter(result_id=id)

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.result = result
            form.save()
            return redirect('/result/' + str(id))
    else:
        form = forms.CommentForm
    return render(request, "result.html",
                  {"result": result,
                   "comments": comments,
                   "form": form})

def raceform(request):
    context = {}

    if request.method == "POST":
        form = forms.RaceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.result = result
            form.save()
            return redirect('/')
    else:
        form = forms.RaceForm
    return render(request, "race-form.html",
                  {"form": form})

def addresult(request):
    context = {}

    if request.method == "POST":
        form = forms.ResultForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.result = result
            form.save()
            return redirect('/')
    else:
        form = forms.ResultForm
    return render(request, "result-form.html",
                  {"form": form})

def comments(request, id):
    context = {}
    try:
        context["comments"] = Comment.objects.filter(result_id=id)
        print(type(Comment.objects.get(result_id=id)))
    except:
        raise Http404("comments does not exist")
    return render(request, 'comments.html', context)