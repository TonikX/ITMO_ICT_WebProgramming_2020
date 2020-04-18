from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from leaderboard.models import Comment


class AddCommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('racer', 'comment_type', 'text')
		labels = {
			'racer': ('Identify who your comment is adressed to'),
			'comment_type': ('Choose the type of your comment'),
			'text': ('Enter your comment'),
		}


class Registration(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	username = forms.CharField(required=True, label='Enter username')
	first_name = forms.CharField(required=True, label='Enter name')
	last_name = forms.CharField(required=True, label='Enter surname')
	email = forms.CharField(required=True, label='Enter e-mail')
	password1 = forms.CharField(required=True, label='Enter password', widget=forms.PasswordInput)
	password2 = forms.CharField(required=True, label='Repeat password', widget=forms.PasswordInput)
