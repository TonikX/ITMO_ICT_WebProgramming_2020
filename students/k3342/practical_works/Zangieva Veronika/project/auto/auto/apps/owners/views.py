from django.http import Http404, HttpResponseRedirect


from django.shortcuts import render 

from .models import Car, Owner, Ownership, License


def index(request):
	owner_data = Owner.objects.all()
	return render(request, 'owners/list.html', {'owner_data': owner_data})
	
def detail(request, owner_id):
	try:
		a = Owner.objects.get( id = owner_id )
	except:
		raise Http404("Owner not found!")

	return render(request, 'owners/detail.html', {'owner': a})
