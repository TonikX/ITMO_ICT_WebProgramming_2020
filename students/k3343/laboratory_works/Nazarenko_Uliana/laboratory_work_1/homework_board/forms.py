from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Teacher, Hometask, Comment, User_profile


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


class Register_student(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = [
            "surname",
            "name",
            "patronymic",
            "group_number",
        ]


class Create_comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "hometask",
            "type_of_comment",
            "type_of_importance",
            "comment",
        ]

        labels = {
            "hometask": ("Укажите домашнее задание, к которому хотите оставить комментарий"),
            "type_of_comment": ("Выберите тип коментария"),
            "type_of_importance": ("Укажите важность комментария"),
            "comment": ("Напишите свой комментарий"),
        }

        widgets = {
            "comment": Textarea(attrs={'cols': 80, 'rows': 5}),
        }