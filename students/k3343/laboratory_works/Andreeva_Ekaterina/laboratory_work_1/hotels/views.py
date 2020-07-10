from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Hotel
from .forms import AddCommentForm


def show_hotels(request):
    """Выод всех отелей"""
    hotels = Hotel.objects.all()
    return render(request, 'all_hotels.html', {"hotels": hotels})


def show_hotel_single(request, pk):
    """Вывод полной информации об авирейсе"""
    hotel = get_object_or_404(Hotel, id=pk)
    comment = Comment.objects.filter(hotel=pk)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.hotel = hotel
            form.save()
            return redirect(show_hotel_single, pk)
    else:
        form = AddCommentForm()
    return render(request, "single_hotel.html",
                  {
                      "hotel": hotel,
                      "comments": comment,
                      "form": form,
                  })
# Create your views here.
