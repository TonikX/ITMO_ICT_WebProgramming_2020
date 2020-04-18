from django import forms
from .models import Homework, Student, Comment
from django.contrib.auth.models import User


class RegUserForm(forms.ModelForm): ###пароль юзер
    class Meta:
        model = User
        help_texts = {
            'username': None,
            'password': "Минимум 8 символов."
        }
        fields = ('username', 'password')
        labels = {'username' : 'Придумай id', 'password': 'Придумай пароль'}

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


class StudentForm(forms.ModelForm): #для добавления фио и группы студента
    class Meta:
        model = Student

        fields = [
            "name",
            "surname",
            "user_id",
            "group_number"
        ]

        labels = {
            "name": ("Имя + Отчество"),
            "surname": ("Фамилия"),
            "user_id": ("Твой id"),
            "group_number": ("Твой номер группы"),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "user",
            "task",
            "importance",
            "type",
            "text"
        ]

        labels = {
            "user": ("Твое имя"),
            "task": ("Домашнее задание"),
            "importance": ("Поставь галочку, если твой комментарий является важным"),
            "type": ("Выбери тип комментария"),
            "text": ("Комментарий"),
        }



