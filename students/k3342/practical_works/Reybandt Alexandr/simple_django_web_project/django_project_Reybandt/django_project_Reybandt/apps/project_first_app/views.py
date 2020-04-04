from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import CarOwner, Ownership, Car
from .forms import OwnerForm

class CarList(ListView):
	model = Car

class CreateCar(CreateView):
	model = Car
	success_url = 'car_model'  
	fields = [
	'make',
	'model',
	'color',
	'state_number',
	]

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

def owners_list(request):
	try:
		context = {}
		context["dataset"] = CarOwner.objects.all()
	except:
		raise Http404("Список пуст")
	
	return render(request, "project_first_app/owners_list.html", context)

def create_view(request):
	context = {}
	form = OwnerForm(request.POST or None)

	if form.is_valid():
		form.save()

	context['form'] = form
	return render(request, "project_first_app/create_view.html", context)