from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Teacher, UserProfile, Hometask, Comment
from .forms import AddComment, Student_reg, RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')


def show_tasks(request):
    tasks = {}
    tasks["tasks"] = Hometask.objects.all()
    return render(request, 'all_tasks.html', tasks)


def show_comments(request):
    comments = {}
    comments["comments"] = Comment.objects.all()
    return render(request, 'all_comments.html', comments)


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile_page')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class StudentReg(CreateView):
    model = UserProfile
    fields = [
        "surname",
        "name",
        "second_name",
        "group",
    ]
    success_msg = 'Профиль пользователя успешно заполнен'
    def as_view(request):
        students = {}
        form = Student_reg(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.isu = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        students['form'] = form
        return render(request, 'registration/profile_page.html', students)


@login_required
class Add_Comment(CreateView):
    model = Comment
    fields = [
            "hometask",
            "type_of_comment",
            "importance_of_comment",
            "text",
        ]
    def as_view(request):
        comments = {}
        form = AddComment(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.student = request.user
            form.save()
            return HttpResponseRedirect(reverse_lazy('all_comments'))
        comments['form'] = form
        return render(request, 'add_comment.html', comments)



# Create your views here.
