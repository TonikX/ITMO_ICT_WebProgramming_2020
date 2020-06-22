from django.shortcuts import render
from .forms import *
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView

# Create your views here.
def main(request):
    return render(request, 'main.html')

class HotelView(ListView):
    model = Hotel

    def get(self, request):
        context = {}

        try:
            context["hotels"] = Hotel.objects.all()
        except Hotel.DoesNotExist:
            raise Http404("Hotel does not exist")

        return render(request, 'hotels.html', context)


def about_hotel(request, hotel_id):
    global user_id
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404("Hotel does not exist")

    try:
        comments = Comment.objects.filter(hotel=hotel_id).all()
    except Comment.DoesNotExist:
        pass

    if request.POST.get('user_id'):
        user_id = int(request.POST.get('user_id'))

    form = CommentForm(request.POST)

    if form.is_valid():

        hotel_form = form.save(commit=False)
        hotel_form.post = form
        hotel_form.conf_id = hotel_id
        hotel_form.username_id = user_id
        hotel_form.save()

        return HttpResponseRedirect('/hotels/{}/'.format(hotel_id))

    return render(request, 'hotel_info.html', {'hotel': hotel, 'comments': comments, 'form': form})