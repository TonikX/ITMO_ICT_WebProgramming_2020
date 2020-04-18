from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class Registration(UserCreationForm):
    username = forms.CharField(required=True, label="Введите имя пользователя")
    first_name = forms.CharField(required=True, label='Введите имя')
    last_name = forms.CharField(required=True, label='Введите фамилию')
    password1 = forms.CharField(required=True, label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','password1', 'password2')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('conference', 'name', 'email', 'body', 'comment_type')