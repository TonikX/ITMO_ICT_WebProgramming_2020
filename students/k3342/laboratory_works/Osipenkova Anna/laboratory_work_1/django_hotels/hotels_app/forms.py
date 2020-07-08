from django import forms
from .models import HotelComment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    period_start = forms.DateField(label="Начало проживания", required=False )
    period_end = forms.DateField(label="Конец проживания", required=False)
    text = forms.CharField(label="Комментарий", required=False)
    rating = forms.CharField(label="Оценка")
    class Meta:
        model = HotelComment
        fields = [
            "period_start",
            "period_end",
            "text",
            "rating"
        ]
        widgets = {
            "period_start": forms.DateInput(attrs={'type': 'date'}),
            "period_end": forms.DateInput(attrs={'type': 'date'})
        }


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    email = forms.CharField(label="Email адрес")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
