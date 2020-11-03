# from typing import Tuple
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput
from django import forms
# from django.forms import ImageField
# from django.views.generic import CreateView
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


class PublisherForm(forms.ModelForm):
    name = forms.CharField(max_length=120)
    full_another_name = forms.CharField(max_length=240)
    parent = forms.CharField(max_length=300, blank=True, null=True)
    founder = forms.CharField(max_length=300, blank=True, null=True)
    foundation_date = forms.DateField(null=True)
    # director = forms.CheckboxSelectMultiple()
    director = forms.ModelChoiceField(queryset=Director.objects.all(), blank=True, null=True)
    p_slug = forms.CharField(max_length=120)
    email = forms.EmailField(blank=True, null=True)
    website = forms.URLField(blank=True, null=True)
    fact_address = forms.CharField(max_length=240, blank=True, null=True)
    city = forms.CharField(max_length=180, blank=True, null=True)
    country = forms.CharField(max_length=60, blank=True, null=True)
    distribution = forms.CharField(max_length=60, blank=True, null=True)
    about = forms.Textarea()
    logo = forms.ImageField(blank=True, null=True)

    error_massages = {
        'duplicate_publisher': "A publisher with such name already exists",
    }

    name.widget.attrs.update({'class': 'form-control'})
    full_another_name.widget.attrs.update({'class': 'form-control'})
    parent.widget.attrs.update({'class': 'form-control'})
    founder.widget.attrs.update({'type': 'date', 'class': 'form-control'})
    # foundation_date.widget.attrs.update({'class': 'form-control', 'type': 'date', 'value': '2011-08-19',
    # 'id': 'example-date-input'})
    # foundation_date.widgets = {'myDateField': forms.DateInput(attrs={'id': 'datetimepicker1',
    # 'placeholder': 'yyyy-mm-dd'})}
    director.widget.attrs.update({'class': 'form-control form-control-sm'})
    p_slug.widget.attrs.update({'class': 'form-control', 'placeholder': 'this_publisher_name'})
    email.widget.attrs.update({'type': 'text', 'class': 'form-control', 'placeholder': 'Username',
                               'aria-label': 'email', 'aria-describedby': 'basic-addon1'})
    website.widget.attrs.update({'type': 'text', 'class': 'form-control', 'aria-describedby': 'basic-addon2'})
    fact_address.widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
    city.widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})
    # city.widget.attrs.update({'class': 'form-group col-md-6'})
    country.widget.attrs.update({'class': 'form-control', 'placeholder': 'Country'})
    # country.widget.attrs.update({'class': 'form-group col-md-6'})
    distribution.widget.attrs.update({'class': 'form-control', 'placeholder': 'Wordwide'})
    about.attrs.update({'class': 'form-control', 'aria-label': 'With textarea'})
    # logo.widget.attrs.update({'class': 'input-group-prepend'})
    logo.widget.attrs.update({'type': 'file', 'class': 'custom-file-input', 'id': 'inputGroupFile01',
                              'aria-describedby': 'inputGroupFileAddon01'})

    def clean_p_slug(self):
        new_p_slug = self.cleaned_data['p_slug'].lower()  # обязательное поле - ошибки не будет

        if new_p_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Publisher.objects.filter(p_slug__exact=new_p_slug).count():
            # если что-то найдет в словаре инициализируем исключение об обошибке существования создаваемого объекта
            # (для нас главное, чтобы не совпадал url)
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
            p_slug=self.cleaned_data['p-slug'],  # .replace(' ', '_').replace("&", "and").replace("#", ""),
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
    photo = forms.ImageField(blank=True, null=True)
    full_name = forms.CharField(max_length=1500)
    short_name = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100, blank=True, null=True)
    birth = forms.DateField(blank=True, null=True)
    death = forms.DateField(blank=True, null=True)
    a_slug = forms.CharField(max_length=120)
    email = forms.EmailField(blank=True, null=True)
    website = forms.URLField(blank=True, null=True)
    career = forms.CharField(blank=True, null=True)
    direction = forms.CharField(blank=True, null=True)
    a_ganre = forms.CharField(max_length=300, blank=True, null=True)

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

    email.widget.attrs.update(
        {'type': 'text', 'class': 'form-control', 'placeholder': 'Username', 'aria-label': 'email',
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
    title = forms.CharField(blank=True, null=True)
    orig_lang = forms.ChoiceField(choices=LANGS)
    trans_lang = forms.ChoiceField(choices=LANGS, blank=True, null=True)

    editor = forms.CharField(blank=True, null=True)
    translator = forms.CharField(blank=True, null=True)
    narrator = forms.CharField(blank=True, null=True)
    illustrator = forms.CharField(blank=True, null=True)
    authors = forms.ModelChoiceField(queryset=Author.objects.all(), blank=True, null=True)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), blank=True, null=True)
    publication_date = forms.SelectDateWidget(blank=True, null=True)

    type_cover = forms.ChoiceField(choices=COVER_TYPE, blank=True, null=True)
    cover = forms.ImageField(blank=True, null=True)

    b_slug = forms.SlugField()
    b_ganre = forms.CharField(blank=True, null=True)
    descr = forms.Textarea(blank=True, null=True)

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
        fields = ['cover', 'orig_lang_name', 'orig_lang', 'title', 'trans_lang', 'editor', 'translator', 'narrator',
                  'illustrator',
                  'authors', 'publisher', 'publication_date', 'type_cover', 'cover', 'b_slug', 'b_ganre', 'descr']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'type', 'place_author', 'place_book', 'place_publisher', 'place_shop',
                  'importance', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 10}),
        }


class UserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    type_user = forms.ChoiceField(choices=USER_TYPE)
    photo = forms.ImageField()
    uniq_num = forms.CharField()
    location = forms.CharField()
    nationality = forms.CharField()

    first_name.widget.attrs.update({'class': 'form-control'}),
    last_name.widget.attrs.update({'class': 'form-control'}),
    type_user.widget.attrs.update({'class': 'form-control form-control-sm'}),
    photo.widget.attrs.update({'type': 'file', 'class': 'custom-file-input', 'id': 'inputGroupFile01',
                               'aria-describedby': 'inputGroupFileAddon01'}),
    uniq_num.widget.attrs.update({'class': 'form-control'}),
    location.widget.attrs.update({'class': 'form-control'}),
    nationality.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'type_user', 'photo', 'uniq_num', 'location', 'nationality']


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


class Registration(UserCreationForm):
    class Meta:
        # model = User
        model = UserProfile
        # fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        fields = ['first_name', 'last_name', 'type_user', 'photo', 'uniq_num', 'location', 'nationality']

    username = forms.CharField(required=True, label='Enter username')
    first_name = forms.CharField(required=True, label='Enter name')
    last_name = forms.CharField(required=True, label='Enter surname')
    email = forms.CharField(required=True, label='Enter e-mail')
    password1 = forms.CharField(required=True, label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Repeat password', widget=forms.PasswordInput)
