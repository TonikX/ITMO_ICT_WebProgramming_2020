from django import forms
from homework_app.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = [
            "text",
            "type",
            "importance",
        ]
