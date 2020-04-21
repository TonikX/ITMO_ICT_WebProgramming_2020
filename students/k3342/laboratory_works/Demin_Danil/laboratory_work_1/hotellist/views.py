from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Hotel, Comment
from .forms import CommentForm

def hotels(request):
    hotels = {'hotels': Hotel.objects.all()}
    return render(request, 'hotels.html', hotels)

def comments(request, key):
    hotel = get_object_or_404(Hotel, id=key)
    data = {'hotel': hotel, 'comments': Comment.objects.filter(hotel=key)}
    return render(request, 'comments.html', data)

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('hotels')
    template_name = 'registration/register.html'

@login_required
class NewCommentView(CreateView):
    model = Comment
    fields = ["hotel",
              "rating",
              "start_date",
              "end_date",
              "comment"]

    def as_view(request):
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('comments'))
        context = {'form': form}
        return render(request, 'new_comment.html', context)

