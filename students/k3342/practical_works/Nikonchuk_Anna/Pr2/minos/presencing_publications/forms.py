from django import forms
from django.views.generic import CreateView
from django.core.exceptions import ValidationError
from presencing_publications.models import *


class PublisherForm(forms.ModelForm):
    name = forms.CharField(max_length=120)
    full_another_name = forms.CharField(max_length=240)
    parent = forms.CharField(max_length=300)
    founder = forms.CharField(max_length=300)
    foundation_date = forms.SelectDateWidget()
    #director = forms.CheckboxSelectMultiple()
    director = forms.ModelChoiceField(queryset=Director.objects.all())
    p_slug = forms.CharField(max_length=120)
    email = forms.EmailField()
    website = forms.URLField()
    fact_address = forms.CharField(max_length=240)
    city = forms.CharField(max_length=180)
    country = forms.CharField(max_length=60)
    distribution = forms.CharField(max_length=60)
    about = forms.Textarea()
    logo = forms.ImageField()

    publishers = Publisher.objects.all()

    error_massages = {
        'duplicate_publisher': "A publisher with such name already exists",
    }

    name.widget.attrs.update({'class': 'form-control'})
    full_another_name.widget.attrs.update({'class': 'form-control'})
    parent.widget.attrs.update({'class': 'form-control'})
    founder.widget.attrs.update({'type': 'date', 'class': 'form-control'})
    foundation_date.attrs.update({'type': 'date', 'class': 'form-control', 'placeholder': 'yyyy-mm-dd'})
    # foundation_date.widgets = {'myDateField': forms.DateInput(attrs={'id': 'datetimepicker1', 'placeholder': 'yyyy-mm-dd'})}
    director.widget.attrs.update({'class': 'form-control form-control-sm'})
    p_slug.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'type': 'text', 'class': 'form-control', 'placeholder': 'Username', 'aria-label': 'email', 'aria-describedby': 'basic-addon1'})
    website.widget.attrs.update({'type': 'text', 'class': 'form-control', 'aria-describedby': 'basic-addon2'})
    fact_address.widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
    city.widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})
    # city.widget.attrs.update({'class': 'form-group col-md-6'})
    country.widget.attrs.update({'class': 'form-control', 'placeholder': 'Country'})
    # country.widget.attrs.update({'class': 'form-group col-md-6'})
    distribution.widget.attrs.update({'class': 'form-control', 'placeholder': 'Wordwide'})
    about.attrs.update({'class': 'form-control', 'aria-label': 'With textarea'})
    # logo.widget.attrs.update({'class': 'input-group-prepend'})
    logo.widget.attrs.update({'type': 'file', 'class': 'custom-file-input', 'id': 'inputGroupFile01', 'aria-describedby': 'inputGroupFileAddon01'})

    def clean_p_slug(self):
        new_p_slug = self.cleaned_data['p_slug'].lower()  # обязательное поле - ошибки не будет

        if new_p_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_p_slug

    def save(self):
        new_p = Publisher.objects.create(
            name=self.cleaned_data['name'],
            full_another_name=self.cleaned_data['full_another_name'],
            parent=self.cleaned_data['parent'],
            founder=self.cleaned_data['founder'],
            director=self.cleaned_data['director'],
            p_slug=self.cleaned_data['name'].replace(' ', '_').replace("&", "and").replace("#", ""),
            email=self.cleaned_data['email'],
            website=self.cleaned_data['website'],
            fact_address=self.cleaned_data['fact_address'],
            city=self.cleaned_data['city'],
            country=self.cleaned_data['country'],
            distribution=self.cleaned_data['distribution'],
            about=self.cleaned_data['about'],
            logo=self.cleaned_data['logo']
        )
        return new_p

    class Meta:
        model = Publisher
        # fields = ['logo', 'name', 'full_another_name', 'parent']
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    name = forms.CharField()
    author_field = forms.ImageField()

    class Meta:
        model = Author
        fields = ['photo', 'short_name', 'birth', 'death', 'website', 'career', 'direction', 'a_ganre']


class BookForm(CreateView):
    name = forms.CharField()
    book_field = forms.ImageField()
    fields = ['cover', 'orig_lang_name', 'orig_lang', 'title', 'trans_lang']


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
