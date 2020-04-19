from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel
from .models import Comment
from .forms import CommentForm

def hotels_list(request):
    context = {}
    context["dataset"] = Hotel.objects.all()
    return render(request, "hotels_list.html", context)

def hotel_single(request, pk):
    """Вывод отдельного отеля
    """
    hotel = get_object_or_404(Hotel, id=pk)
    comment = Comment.objects.filter(hotel=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.hotel = hotel
            form.save()
            return redirect(hotel_single, pk)
    else:
        form = CommentForm()
    return render(request, "hotel_single.html",
                  {"hotel": hotel,
                   "comment": comment,
                   "form": form})

