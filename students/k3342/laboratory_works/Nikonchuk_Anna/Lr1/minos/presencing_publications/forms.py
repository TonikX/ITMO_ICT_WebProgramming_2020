# from typing import Tuple
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput
from django import forms
# from django.forms import ImageField
# from django.views.generic import CreateView
from django.core.exceptions import ValidationError
from presencing_publications.models import *
from django.core.exceptions import NON_FIELD_ERRORS


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
        widgets = {
            'full_name': forms.CharField.widget(attrs={'class': 'form-control'}),
            'short_name': forms.CharField.widget(attrs={'class': 'form-control'}),
            'first_name': forms.CharField.widget(attrs={'class': 'form-control'}),
            'second_name': forms.CharField.widget(attrs={'class': 'form-control'}),
            'birth': forms.CharField.widget(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'death': forms.CharField.widget(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'a_slug': forms.CharField.widget(attrs={'class': 'form-control', 'placeholder': 'birthYear_Short_Name'}),
            'email': forms.EmailField.widget(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Username',
                                                    'aria-label': 'email', 'aria-describedby': 'basic-addon1'}),
            'website': forms.URLField.widget(attrs={'type': 'text', 'class': 'form-control', 'aria-describedby': 'basic-addon2'}),
            'career': forms.CharField.widget(attrs={'class': 'form-control'}),
            'direction': forms.CharField.widget(attrs={'class': 'form-control'}),
            'a_ganre': forms.CharField.widget(attrs={'class': 'form-control'})
        }


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['cover', 'orig_lang_title', 'orig_lang', 'title', 'trans_lang', 'editor', 'translator',
                  'narrator', 'illustrator', 'authors', 'publisher', 'publication_date', 'type_cover',
                  'cover', 'b_slug', 'b_ganre', 'descr']
        widgets = {
            'orig_lang_title': forms.CharField.widget(attrs={'class': 'form-control'}),
            'title': forms.CharField.widget(attrs={'class': 'form-control'}),
            'editor': forms.CharField.widget(attrs={'class': 'form-control'}),
            'translator': forms.CharField.widget(attrs={'class': 'form-control'}),
            'narrator': forms.CharField.widget(attrs={'class': 'form-control'}),
            'illustrator': forms.CharField.widget(attrs={'class': 'form-control'}),
            'publication_date': forms.CharField.widget(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'b_slug': forms.CharField.widget(attrs={'class': 'form-control', 'placeholder': 'NC_' + str(Book.objects.latest('id').id + 1) + '_Book_Name'}),
            'b_ganre': forms.CharField.widget(attrs={'class': 'form-control'}),
            'descr': forms.Textarea(attrs={'class': 'form-control', 'aria-label': 'With textarea'}),
            # 'cover': forms.ImageField.widget(attrs={'type': 'file',
            #                                 'class': 'custom-file-input',
            #                                 'id': 'inputGroupFile01',
            #                                 'aria-describedby': 'inputGroupFileAddon01'}),
            'orig_lang': forms.ModelChoiceField.widget(attrs={'class': 'form-control form-control-sm'}),
            'trans_lang': forms.ModelChoiceField.widget(attrs={'class': 'form-control form-control-sm'}),
            'publisher': forms.ModelChoiceField.widget(attrs={'class': 'form-control form-control-sm'}),
            'type_cover': forms.ModelChoiceField.widget(attrs={'class': 'form-control form-control-sm'}),
            'authors': forms.ModelMultipleChoiceField.widget(attrs={'class': 'form-control form-control-sm'})
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def clean_p_slug(self):
        new_b_slug = self.cleaned_data['b_slug'].lower()  # обязательное поле - ошибки не будет

        if new_b_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Book.objects.filter(b_slug__iexact=new_b_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_b_slug))
        return new_b_slug

    """
    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['authors'] = [t.pk for t in kwargs['instance'].authors_set.all()]

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)
        old_save_m2m = self.save_m2m
        def save_m2m():
            old_save_m2m()
            instance.authors_set.clear()
            instance.authors_set.add(*self.cleaned_data['authors'])
        self.save_m2m = save_m2m
        if commit:
            instance.save()
            self.save_m2m()
        return instance"""


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
