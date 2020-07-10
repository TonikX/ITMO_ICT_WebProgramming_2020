from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile, Tours, Agency, Comment
from .forms import Comment, RegistrationTourist, Register, NewComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')


def show_tours(request):
    tours = {}
    tours["tours"] = Tours.objects.all()
    return render(request, 'tours.html', tours)


def show_comments(request):
    comments = {}
    comments["comments"] = Comment.objects.all()
    return render(request, 'comments.html', comments)


class RegisterView(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = Register
    success_url = reverse_lazy('profile')
    success_msg = 'Пользователь успешно зарегистрирован'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username,password=password)
        login(self.request, auth_user)
        return form_valid


class TouristRegistration(CreateView):
    model = UserProfile
    fields = [
        "name",
        "surname",
        "country_live",
    ]
    success_msg = 'Профиль успешно заполнен'
    def as_view(request):
        tourists = {}
        form = RegistrationTourist(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.login = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        tourists['form'] = form
        return render(request, 'registration/profile.html', tourists)


@login_required
class New_Comment(CreateView):
    model = Comment
    fields = [
            "tour",
            "type_of_comment",
            "text",
        ]
    def as_view(request):
        comments = {}
        form = NewComment(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.tourist = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('comments'))
        comments['form'] = form
        return render(request, 'new_comment.html', comments)
