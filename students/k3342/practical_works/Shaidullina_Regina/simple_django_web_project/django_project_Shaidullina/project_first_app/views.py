from django.shortcuts import render
from django.http import Http404, HttpResponse
from project_first_app.models import Owner, Car, Ownership, DriversLicense
from django.views.generic.list import ListView
from project_first_app.forms import OwnerForm
from django.views.generic.edit import CreateView


# Create your views here.

def query(request, car_id=2):
	try:
		car = Car.objects.filter(id=car_id).first()
		info = Ownership.objects.filter(car_id=car_id)
		owner_ids = [owner.owner_id for owner in info]
		owners_info = Owner.objects.filter(id__in=owner_ids)
		dl_info = DriversLicense.objects.filter(owner_id__in=owner_ids)
		ownership_info = Ownership.objects.filter(owner_id__in=owner_ids, car_id=car_id)
	except Car.DoesNotExist:
		raise Http404('Car does not exist.')
	return render(request, 'owner.html', {'car_info': car, 'info': zip(owners_info, dl_info, ownership_info)})


def output(request, owner_id):
	try:
		owner = Owner.objects.filter(id=owner_id)
	except Owner.DoesNotExist:
		raise Http404('Owner does not exist.')
	return render(request, 'output.html', {'owner': owner, 'id': owner_id})


# Task 2.1
def all_owners(request):
	try:
		owners = Owner.objects.all()
	except Owner.DoesNotExist:
		raise Http404('Owner does not exist.')
	return render(request, 'owners.html', {'owners': owners})


# Task 2.2
class CarsList(ListView):
	model = Car


# Task 3.1
def input_owners(request):
	context = {}
	form = OwnerForm(request.POST or None)
	if form.is_valid():
		form.save()
	context['form'] = form
	return render(request, "owners_form.html", context)


# Task 3.2
class CarCreate(CreateView):
	model = Car
	fields = ['brand', 'model', 'colour', 'car_number']
