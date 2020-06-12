from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment

		fields = [
			"start_date",
			"end_date",
			"text",
			"rating"
		]

		widgets = {
			"start_date": forms.DateInput(attrs={'type': 'date'}),
			"end_date": forms.DateInput(attrs={'type': 'date'})
		}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
        	'username',
        	'password',
        	'email',
        	'first_name',
        	'last_name'
        ]
