from django import forms
from .models import HotelComment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
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
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
