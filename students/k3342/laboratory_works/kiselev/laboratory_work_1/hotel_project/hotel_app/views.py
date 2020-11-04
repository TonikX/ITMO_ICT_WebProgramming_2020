from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
class HotelAllView(ListView):
    model = Hotel

    def get(self, request):
        context = {}

        try:
            context["hotels"] = Hotel.objects.all()
        except Flight.DoesNotExist:
            raise Http404("Такого отеля не существует")

        return render(request, 'hotel_list.html', context)


@login_required
def show_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(id=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404("Такого отеля не существует")

    try:
        flats = Flat.objects.filter(hotel=hotel_id).all()
    except Flat.DoesNotExist:
        pass  

    try:
    	comments = Comment.objects.filter(hotel=hotel_id).all()
    except Comment.DoesNotExist:
        pass

    if request.POST.get('user'):
	    user_id = int(request.POST.get('user'))

    form = CommentForm(request.POST)

    if form.is_valid():

        new_form = form.save(commit=False)
        new_form.post = form
        new_form.hotel_id = hotel_id
        new_form.user_id = user_id
        new_form.save()

        return HttpResponseRedirect('./{}'.format(hotel_id))

    return render(request, 'hotel.html', {'hotel': hotel, 'flats': flats, 'comments': comments, 'form': form})


def user_register(request):
    registered = False

    if request.method == 'POST':

        user_register_user = UserForm(data=request.POST)

        if user_register_user.is_valid():

            user = user_register_user.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:

            print(user_register_user.errors)
    else:

        user_register_user = UserForm()

    return render(request,'user_register.html', {'user_register_user': user_register_user, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../hotels/all')

            else:
                return HttpResponse("Your account was inactive.")

        else:
            return HttpResponse("Invalid login")

    else:
        return render(request, 'user_login.html', {})
