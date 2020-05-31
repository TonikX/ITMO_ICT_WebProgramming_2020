from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Teacher, User_profile, Hometask, Comment
from .forms import Create_comment, Register_student, RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')


def hw_view(request):
    hw = {}
    hw["hw"] = Hometask.objects.all()
    return render(request, 'hw_list.html', hw)


def comments_view(request):
    comments = {}
    comments["comments"] = Comment.objects.all()
    return render(request, 'comments_list.html', comments)


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class User_registration(CreateView):
    model = User_profile
    fields = [
        "surname",
        "name",
        "patronymic",
        "group_number",
    ]
    success_msg = 'Данные пользователя успешно внесены'

    def as_view(request):
        students = {}
        form = Register_student(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.id_user = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        students['form'] = form
        return render(request, 'registration/profile.html', students)


@login_required
class Comment_creation(CreateView):
    model = Comment
    fields = [
            "hometask",
            "type_of_comment",
            "importance_of_comment",
            "text",
        ]

    def as_view(request):
        comments = {}
        form = Create_comment(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('commentslist'))
        comments['form'] = form
        return render(request, 'comment_creation.html', comments)
