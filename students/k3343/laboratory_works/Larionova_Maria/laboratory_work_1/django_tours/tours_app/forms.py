from django import forms
from .models import TourComment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = TourComment
		fields = [
			"question_type",
			"comment_text"
		]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')
