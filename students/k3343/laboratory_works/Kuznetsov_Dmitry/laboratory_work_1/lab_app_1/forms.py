from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.forms import Textarea

from .models import Comment




class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=50, required=True, label="Введите логин", error_messages={'required': 'Обязательное поле'})

    first_name = forms.CharField(max_length=50, required=True, label="Введите имя", error_messages={'required': 'Обязательное поле'})

    last_name = forms.CharField(max_length=50, required=True, label="Введите фамилию", error_messages={'required': 'Обязательное поле'})

    password1 = forms.CharField(max_length=50, required=True, label="Введите пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})

    password2 = forms.CharField(max_length=50, required=True, label="Повторите пароль", widget=forms.PasswordInput, error_messages={'required': 'Обязательное поле'})



    class Meta:


        model = User


        fields = ('username', 'first_name', 'last_name','password1', 'password2', )




class CommentForm(forms.ModelForm):





    TYPES = (


        ('Выход на посадку', 'Изменение выхода на посадку'),


        ('Что-то не то с рейсом', 'Проблемы с рейсом'),





        ('Потеряшка', 'Потерявшийся пассажир'),


    )






    class Meta:


        model = Comment


        fields = [
            "text",
            "kind",

        ]

        labels = {
            "text": ("Введите комментарий"),
            "kind": ("Выберите тип комментария"),
        }

        widgets = {
            "text" : Textarea(attrs={'cols': 70, 'rows': 10}),
        }