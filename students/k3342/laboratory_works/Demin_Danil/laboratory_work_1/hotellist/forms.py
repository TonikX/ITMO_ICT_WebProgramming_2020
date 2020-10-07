from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, DateInput
from .models import Comment

class RegisterUserForm(ModelForm):
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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            "hotel",
            "start_date",
            "end_date",
            "rating",
            "comment"
        ]
        labels = {
            "hometask": ("Choose the hotel you stayed at:"),
            "start_date": ("Your arrival date:"),
            "end_date": ("Your departure date:"),
            "rating": ("Rate the hotel"),
            "comment": ("Your comment:")
        }
        widgets = {"comment" : Textarea(attrs={'cols': 50, 'rows': 5}),
                   "start_date": DateInput(attrs={'type': 'date'}),
                   "end_date": DateInput(attrs={'type': 'date'})}