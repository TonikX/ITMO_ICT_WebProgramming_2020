from django import forms
from .models import Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password')


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			"comment_type",
			"desc"
		]
