from typing import Tuple

from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms import ImageField
from django.views.generic import CreateView
from django.core.exceptions import ValidationError
from presencing_publications.models import *


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ['full_name', 'short_name', 'first_name', 'last_name']
        # fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class PublisherForm(forms.Form):
    name = forms.CharField(max_length=120)
    full_another_name = forms.CharField(max_length=240)
    parent = forms.CharField(max_length=300)
    founder = forms.CharField(max_length=300)
    foundation_date = forms.DateField()
    # director = forms.CheckboxSelectMultiple()
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
    # foundation_date.widget.attrs.update({'class': 'form-control', 'type': 'date', 'value': '2011-08-19', 'id': 'example-date-input'})
    # foundation_date.widgets = {'myDateField': forms.DateInput(attrs={'id': 'datetimepicker1', 'placeholder': 'yyyy-mm-dd'})}
    director.widget.attrs.update({'class': 'form-control form-control-sm'})
    p_slug.widget.attrs.update({'class': 'form-control', 'placeholder': 'this_publisher_name'})
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
        if Publisher.objects.filter(p_slug__exact=new_p_slug).count():
        # если что-то найдет в словаре инициализируем исключение об обошибке существования создаваемого объекта (для нас главное, чтобы не совпадал url)
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_p_slug))

        return new_p_slug

    # у ModelForm есть свой save метод, данная реализация используется для примера
    # но на самом деле он излишний и будет каждый раз создавать новый об
    def save(self):
        new_p = Publisher.objects.create(
            name=self.cleaned_data['name'],
            full_another_name=self.cleaned_data['full_another_name'],
            parent=self.cleaned_data['parent'],
            founder=self.cleaned_data['founder'],
            foundation_date=self.cleaned_data['foundation_date'],
            director=self.cleaned_data['director'],
            p_slug=self.cleaned_data['p-slug'],  #.replace(' ', '_').replace("&", "and").replace("#", ""),
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

        widgets = {
            'foundation_date': DatePickerInput()
        }


class AuthorForm(forms.ModelForm):
    photo = forms.ImageField()
    full_name = forms.CharField()
    short_name = forms.CharField()
    first_name = forms.CharField()
    second_name = forms.CharField()
    birth = forms.DateField()
    death = forms.DateField()
    a_slug = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()
    career = forms.CharField()
    direction = forms.CharField()
    a_ganre = forms.CharField()

    photo.widget.attrs.update({'type': 'file', 'class': 'custom-file-input', 'id': 'inputGroupFile01',
                          'aria-describedby': 'inputGroupFileAddon01'})
    full_name.widget.attrs.update({'class': 'form-control'})
    short_name.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    second_name.widget.attrs.update({'class': 'form-control'})
    a_slug.widget.attrs.update({'class': 'form-control'})
    career.widget.attrs.update({'class': 'form-control'})
    direction.widget.attrs.update({'class': 'form-control'})
    a_ganre.widget.attrs.update({'class': 'form-control'})
    
    email.widget.attrs.update({'type': 'text', 'class': 'form-control', 'placeholder': 'Username', 'aria-label': 'email',
               'aria-describedby': 'basic-addon1'})
    website.widget.attrs.update({'type': 'text', 'class': 'form-control', 'aria-describedby': 'basic-addon2'})
    


    def clean_p_slug(self):
        new_a_slug = self.cleaned_data['a_slug'].lower()  # обязательное поле - ошибки не будет

        if new_a_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Author.objects.filter(a_slug__exact=new_a_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_a_slug))
        return new_a_slug

    class Meta:
        model = Author
        fields = ['photo', 'full_name', 'short_name', 'first_name', 'second_name', 'birth', 'death', 'a_slug',
                  'email', 'website', 'career', 'direction', 'a_ganre']
        # fields = '__all__'


class BookForm(forms.ModelForm):
    orig_lang_name = forms.CharField()
    title = forms.CharField()
    orig_lang = forms.ChoiceField(choices=LANGS)
    trans_lang = forms.ChoiceField(choices=LANGS)

    editor = forms.CharField()
    translator = forms.CharField()
    narrator = forms.CharField()
    illustrator = forms.CharField()
    authors = forms.ModelChoiceField(queryset=Author.objects.all())
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    publication_date = forms.SelectDateWidget()

    type_cover = forms.ChoiceField(choices=TYPE_COVER)
    cover = forms.ImageField()

    b_slug = forms.SlugField()
    b_ganre = forms.CharField()
    descr = forms.Textarea()

    cover.widget.attrs.update({'type': 'file', 'class': 'custom-file-input', 'id': 'inputGroupFile01',
                               'aria-describedby': 'inputGroupFileAddon01'})

    def clean_p_slug(self):
        new_b_slug = self.cleaned_data['b_slug'].lower()  # обязательное поле - ошибки не будет

        if new_b_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Book.objects.filter(a_slug__exact=new_b_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_b_slug))
        return new_b_slug

    class Meta:
        model = Book
        fields = ['cover', 'orig_lang_name', 'orig_lang', 'title', 'trans_lang', 'editor', 'translator', 'narrator', 'illustrator',
                  'authors', 'publisher', 'publication_date', 'type_cover', 'cover', 'b_slug', 'b_ganre', 'descr']
