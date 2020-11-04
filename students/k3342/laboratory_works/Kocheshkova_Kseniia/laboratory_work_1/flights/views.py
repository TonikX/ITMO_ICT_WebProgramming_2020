from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Person, Ticket, Flight, Comment, Reservation
from .forms import CommentForm, ReservationForm
from django.http import Http404


def person_info(request, person_id):
    try:
        p = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'person.html', {'person': p})


def person_list(request):
    context = {'dataset': Person.objects.all()}
    return render(request, "person_list.html", context)


def flights(request):
    flights = {'flights': Flight.objects.all()}
    return render(request, 'flights.html', flights)


def reservations(request, key):
    flight = get_object_or_404(Flight, id=key)
    data = {'flight': flight, 'reservations': Reservation.objects.filter(id=key)}
    return render(request, 'reservations.html', data)


class TicketList(ListView):
    cost = Ticket

def comments(request, key):
    flight = get_object_or_404(Flight, id=key)
    data = {'flight': flight, 'comments': Comment.objects.filter(id=key)}
    return render(request, 'comments.html', data)


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('flights')
    template_name = 'registration/register.html'


@login_required
class NewCommentView(CreateView):
    model = Comment
    fields = [
            "name_flight",
            "registration_evaluation",
            "flight_evaluation",
            "personnel_assessment",
            "category",
            "comment",
            "departure_date"]

    def as_view(request):
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_author = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('flights'))
        context = {'form': form}
        return render(request, 'new_comment.html', context)


@login_required
class NewReservationView(CreateView):
    model = Reservation
    fields = [
            "name_flight",
            "full_name",
            "passport_number",
            "phone_number",
            "category",
            "row",
            "place",
            "date_of_departure"]

    def as_view(request):
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_author = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('flights'))
        context = {'form': form}
        return render(request, 'new_reservation.html', context)
