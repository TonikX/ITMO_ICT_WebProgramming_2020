from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from auto_racing_scoreboard.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('racer', 'comment_type', 'text')
        labels = {
            'racer': ('Выберите, кому адресован ваш комментарий'),
            'comment_type': ('Выберите тип комментария'),
            'text': ('Напишите комментарий'),
        }

    widgets = {
        "text": Textarea(attrs={'cols': 60, 'rows': 5}),
    }


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'surname', 'name', 'patronymic', 'email', 'password1', 'password2')

    username = forms.CharField(required=True, label='Придумайте логин')
    surname = forms.CharField(required=True, label='Введите фамилию')
    name = forms.CharField(required=True, label='Введите имя')
    patronymic = forms.CharField(required=True, label='Введите отчество')
    email = forms.CharField(required=True, label='Введите e-mail')
    password1 = forms.CharField(required=True, label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Повторите пароль', widget=forms.PasswordInput)
