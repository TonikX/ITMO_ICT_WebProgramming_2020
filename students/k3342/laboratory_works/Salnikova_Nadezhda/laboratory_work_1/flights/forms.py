from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from flights.models import Client, Comment


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ClientRegister(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'bonus_card']


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['flight', 'comment_type', 'text']

    labels = {
        'flight': ('Chose a flight to leave a comment'),
        'type_of_comment': ('Choose the comment type'),
        'text': ('Type your comment'),
    }

    widgets = {
        "text": Textarea(attrs={'cols': 70, 'rows': 10}),
    }
