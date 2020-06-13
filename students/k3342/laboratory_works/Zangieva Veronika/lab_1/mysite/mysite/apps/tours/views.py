from django.shortcuts import render, redirect
from django.http import Http404
from .models import Tour, Comment
from django.views.generic.list import ListView
from tours.forms import CommentForm

def tour(request, tour_id):
    p = Tour.objects.get(pk=tour_id)
    context = {"dataset": Comment.objects.filter(tour=p), "tour": p}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.tour = p
            form.save()
        return redirect("tour_one", tour_id)
    else:
        form = CommentForm()
    context["form"] = form
    return render(request, 'tour.html', context)

class TourList(ListView):

    model = Tour

