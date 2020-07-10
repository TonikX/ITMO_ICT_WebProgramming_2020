from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
class HotelListView(ListView):
    model = Hotel

    def get(self, request):
        context = {}

        try:
            context["hotels"] = Hotel.objects.all()
        except Flight.DoesNotExist:
            raise Http404("Отель не найден")

        return render(request, 'hotels_all.html', context)


@login_required
def get_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(id=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404("Отель не найден")

    try:
        rooms = Room.objects.filter(hotel=hotel_id).all()
    except Room.DoesNotExist:
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

    return render(request, 'hotel.html', {'hotel': hotel, 'rooms': rooms, 'comments': comments, 'form': form})


def register(request):
    is_registered = False

    if request.method == 'POST':

        reg_data = UserForm(data=request.POST)

        if reg_data.is_valid():

            user = reg_data.save()
            user.set_password(user.password)
            user.save()
            is_registered = True

        else:

            print(reg_data.errors)
    else:

        reg_data = UserForm()

    return render(request,'register.html', {'reg_data': reg_data, 'is_registered': is_registered})


def set_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hotels/list')

            else:
                return HttpResponse("Ваш аккаунт ещё не активирован, обратитесь к администратору.")

        else:
            return HttpResponse("Неправильный логин")

    else:
        return render(request, 'login.html', {})
