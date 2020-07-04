from django.shortcuts import render
from django.http import Http404
from .models import Car,Owner,Ownership
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import OwnerForm

def about_owner(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})

class CarList(ListView):
	model = Car

def owner_list(request):
	try:
		owners = Owner.objects.all()
	except:
		raise Http404("Список пуст")

	return render(request, "owner_list.html",{"owner_list": owners})

def add_owner(request):
    context ={}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "add_owner.html", context)

class AddCar(CreateView):
	model = Car
	success_url = '/add_car/'
	fields = [
	'brand',
	'model',
	'color',
	'plate',
	]