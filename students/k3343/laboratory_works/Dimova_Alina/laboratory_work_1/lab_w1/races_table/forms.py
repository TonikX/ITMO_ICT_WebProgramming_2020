from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text',
            'type',
        ]
        labels = {
            'type': 'Выберите тип комментария',
            'text': 'Введите текст комментария',
        }


class UserRegistrForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Введите имя пользователя')
    first_name = forms.CharField(required=True, label='Введите ваше имя')
    last_name = forms.CharField(required=True, label='Введите вашу фамилию')
    email = forms.CharField(required=True, label='Введите адрес эл. почты')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Введите имя пользователя')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
