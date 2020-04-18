from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
class HotelView(ListView):
    model = Hotel

    def get(self, request):
        context = {}

        try:
            context["hotels"] = Hotel.objects.all()
        except Flight.DoesNotExist:
            raise Http404("Hotel does not exist")

        return render(request, 'hotels.html', context)


@login_required
def hotel_info(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404("Hotel does not exist")

    try:
        rooms = Room.objects.filter(hotel=hotel_id).all()
    except Room.DoesNotExist:
        pass  

    try:
    	comments = HotelComment.objects.filter(hotel=hotel_id).all()
    except HotelComment.DoesNotExist:
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

        return HttpResponseRedirect('/hotels/{}/'.format(hotel_id))

    return render(request, 'hotel.html', {'hotel': hotel, 'rooms': rooms, 'comments': comments, 'form': form})


def register(request):
    registered = False

    if request.method == 'POST':

        create_user_form = UserForm(data=request.POST)

        if create_user_form.is_valid():

            user = create_user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:

            print(create_user_form.errors)
    else:

        create_user_form = UserForm()

    return render(request,'register.html', {'create_user_form': create_user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hotels/')

            else:
                return HttpResponse("Your account was inactive.")

        else:
            return HttpResponse("Invalid login")

    else:
        return render(request, 'login.html', {})
