from django.http import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render 
from django.views.generic.edit import CreateView
from .models import CarsModel
#from .models import OwnersModel
#from .forms import OwnersForm
# 1. Представления Функционально
#def index(request):
#	owner_data = OwnersModel.objects.all()
#	return render(request, 'owners/list.html', {'owner_data': owner_data})

# 2. Представления На основе классов

#class CarsList(ListView):
	#model = CarsModel

#3. Форма функционально
#def create_view(request):
#	context = {} 
#	form = OwnersForm(request.POST or None)
#	if form.is_valid():
#		form.save()
#	context['form'] = form
#	return render(request, "owners/create_view.html", context)

#4. Форма на основе классов
class CarsCreate(CreateView):
	model = CarsModel
	fields = ['mark', 'c_type', 'color', 'gov_num']






