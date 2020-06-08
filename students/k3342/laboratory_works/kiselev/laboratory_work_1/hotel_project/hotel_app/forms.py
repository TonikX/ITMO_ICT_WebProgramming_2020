from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			"date_start",
			"date_end",
			"text",
			"star"
		]
		widgets = {
			"date_start": forms.DateInput(attrs={'type': 'date'}),
			"date_end": forms.DateInput(attrs={'type': 'date'})
		}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
