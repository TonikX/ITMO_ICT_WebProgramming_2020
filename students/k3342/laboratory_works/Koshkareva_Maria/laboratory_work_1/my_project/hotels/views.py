from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.list import ListView

from .models import Hotel, Comment
from .forms import CommentForm


class HotelsList(ListView):
    model = Hotel


def hotel_info(request, hotel_id):

    the_hotel = get_object_or_404(Hotel, pk=hotel_id)
    the_comments = Comment.objects.filter(one_hotel=hotel_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.one_hotel = the_hotel
            form.save()
            #return redirect('hotel-info', hotel_id)
    else:
        form = CommentForm()

    return render(request, "hotels/hotel_info.html",
                                            {"hotel":the_hotel,
                                             "the_comments":the_comments,
                                             "form":form})
