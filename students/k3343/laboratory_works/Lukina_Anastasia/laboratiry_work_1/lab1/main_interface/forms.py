from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Введите логин", error_messages={'required': 'Обязательное поле'})
    first_name = forms.CharField(max_length=30, required=True, label="Введите имя", error_messages={'required': 'Обязательное поле'})
    last_name = forms.CharField(max_length=30, required=True, label="Введите фамилию", error_messages={'required': 'Обязательное поле'})
    password1 = forms.CharField(max_length=30, required=True, label="Введите пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})
    password2 = forms.CharField(max_length=30, required=True, label="Повторите пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','password1', 'password2', )


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=3000,required=False, widget=forms.Textarea, label="Введите Ваш комментарий")
    TYPES = (
        ('T1', 'Вопрос о возможности участия'),
        ('T2', 'Вопрос о возможности опубликования'),
        ('T3', 'Вопрос о месте проведения'),
        ('T4', 'Иное')
    )
    comment_type = forms.CharField(max_length=2, widget=forms.Select(choices=TYPES), label="Отметьте тип вопроса", error_messages={'required': 'Обязательное поле'})

    class Meta:
        model = Comment
        fields = ('comment', 'comment_type', )
