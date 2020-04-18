from django import forms
from .models import FlightComments
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = FlightComments
		fields = [
			"com_type",
			"com_text"
		]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
