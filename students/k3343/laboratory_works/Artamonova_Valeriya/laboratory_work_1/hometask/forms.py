from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Teacher, Hometask, Comment, UserProfile


class RegisterUserForm(forms.ModelForm):
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


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "surname",
            "name",
            "second_name",
            "group",
        ]


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "hometask",
            "type_of_comment",
            "importance_of_comment",
            "text",
        ]

        labels = {
            "hometask": ("Выберите домашнее задание, к которому хотите добавить комментарий"),
            "type_of_comment": ("Выберите тип коментария"),
            "importance_of_comment": ("Важность Вашего комментария"),
            "text": ("Введите свой комментарий"),
        }

        widgets = {
            "text" : Textarea(attrs={'cols': 70, 'rows': 10}),
        }




