from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import Registration,  CommentForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Comment, Conference
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def detail(request):
    conf = Conference.objects.all()
    return render(request, 'conf_info.html', {'conf': conf})


def show_conferences(request):
    context={}
    context["dataset"] = Conference.objects.all()
    return render(request, 'all_conferences.html', context)


def comments(request):
    comments= {}
    comments['comments'] = Comment.objects.all()
    form = CommentForm(request.POST)
    comments['form'] = form
    if form.is_valid():
        object = form.save(commit=False)
        object.user = request.user
        object.save()
        return redirect('/all_comments')

    return render(request, "all_comments.html", comments)



def register(request):
    form = Registration(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/all_sections/')
    return render(request, 'registration/register.html', {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = "/all_sections/"

    def form_valid(self, form):

        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutFormView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/all_sections/')


