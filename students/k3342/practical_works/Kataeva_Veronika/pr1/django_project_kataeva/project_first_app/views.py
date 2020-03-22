import datetime
from django.http import Http404 
from django.shortcuts import render
from project_first_app.models import Ownership, Car, Owner


def get_owner(request, c_id):
    try:
        now = datetime.datetime.now()
        date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        ownership = Ownership.objects.filter(car_id=c_id).filter(date_of_start__lte=date).filter(date_of_end__gte=date)[0]
        owner = Owner.objects.get(id=ownership.owner_id)
    except Car.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'owner.html', {'owner': owner})