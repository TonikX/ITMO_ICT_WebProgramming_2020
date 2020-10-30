from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegisterForm, CommentForm
from .models import Hotels, Comments

def hotelsview(request):
	hotels = Hotels.objects.all()
	return render(request, "hotels/hotel_list.html",{"hotel_list": hotels})

def allbthotel(request, pk):
	hotel = Hotels.objects.get(id=pk)
	comments = Comments.objects.filter(hotel=pk).all()
	return render(request, "hotels/hotel_detail.html",{"hotel": hotel, "comment_list": comments})

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("/")
	else:
		form = RegisterForm()
	return render(response, "register/register.html", {"form":form})

def addcomment(request):
	form = CommentForm(request.POST)
	if form.is_valid():
		form = form.save(commit=False)
		form.contact_info = request.user
		form.save()
		return redirect("/")
	return render(request, "hotels/add_comment.html", {"form":form})