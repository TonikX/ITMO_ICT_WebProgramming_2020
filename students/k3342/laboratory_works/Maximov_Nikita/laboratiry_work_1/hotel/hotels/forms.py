from django import forms
from django.forms import ModelForm, Textarea, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = [
        	"hotel",
            "rating",
            "comment_text",
            "start_period",
            "end_period"
        ]
        labels = {
        	"hotel": ("Выберете отель:"),
            "rating": ("Ваша оценка (из 10):"),
            "comment_text": ("Комментарий:"),
            "start_period": ("Дата заезда"),
            "end_period": ("Дата выезда:")
        }
        widgets = {"comment_text" : Textarea(attrs={'cols': 50, 'rows': 5}),
                   "start_period": DateInput(attrs={'type': 'date'}),
                   "end_period": DateInput(attrs={'type': 'date'})}