from django.http import Http404
from django.shortcuts import render
from .models import CarOwner, Ownership

def info(request):
	try:
		query = CarOwner.objects.all()
	except:
		raise Http404("Владельцы не найдены")
	return render(request, 'project_first_app/owners.html', {'owners': query})

def detail(request, ownership_id):
	try:
		query = Ownership.objects.get(id = ownership_id)
	except:
		raise Http404("Что-то пошло не так...")
	return render(request, 'project_first_app/ownership.html', {'ownership': query})

