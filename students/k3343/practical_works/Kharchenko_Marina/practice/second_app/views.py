from django.shortcuts import render
from .models import User
# Create your views here.

def user_list(request):
    context={}

    context["dataset"] = User.objects.all()
    return render(request, "user_list.html", context)