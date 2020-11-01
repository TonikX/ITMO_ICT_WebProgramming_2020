from django.shortcuts import render, get_object_or_404, redirect
from hotels_list.models import Hotels, Reviews, Rooms
from hotels_list.forms import ReviewForm


def hotel_list(request):
    hotels = Hotels.objects.all()
    return render(request, "hotels/hotel_list.html", {"hotels": hotels})


def hotel_single(request, pk):
    hotel = get_object_or_404(Hotels, id=pk)
    rooms = Rooms.objects.filter(room_hotel=pk)
    review = Reviews.objects.filter(review_hotel=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.review_user = request.user
            form.review_hotel = hotel
            form.save()
            return redirect(hotel_single, pk)
    else:
        form = ReviewForm()
    return render(request,
                  "hotels/hotel_single.html",
                  {"hotel": hotel,
                   "rooms": rooms,
                   "reviews": review,
                   "form": form})
