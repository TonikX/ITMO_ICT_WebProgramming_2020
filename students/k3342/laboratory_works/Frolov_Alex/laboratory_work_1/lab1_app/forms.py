from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Comment


class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = [
            "conference_name",
            "type_of_comment",
            "text",
        ]

        labels = {
            "conference_name": ("Выберите конференцию, к которой хотите добавить комментарий"),
            "type_of_comment": ("Выберите тип коментария"),
            "text": ("Введите свой комментарий"),
        }

        widgets = {
            "text" : Textarea(attrs={'cols': 70, 'rows': 10}),
        }