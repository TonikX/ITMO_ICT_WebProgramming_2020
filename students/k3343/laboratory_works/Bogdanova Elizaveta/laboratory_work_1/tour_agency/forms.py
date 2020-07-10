from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import UserProfile, Tours, Comment


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class RegistrationTourist(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "name",
            "surname",
            "country_live",
        ]


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "tour",
            "type_of_comment",
            "text",
        ]

        labels = {
            "tour": ("Выберите тур для добавления комментария"),
            "type_of_comment": ("Выберите тип комментария"),
            "text": ("Текст комментария"),
        }

        widgets = {
            "text" : Textarea(attrs={'cols': 70, 'rows': 10}),
        }
