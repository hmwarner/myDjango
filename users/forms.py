"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
"""
from django.urls import reverse_lazy
from django.core.validators import RegexValidator
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
"""
class NameWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        super().__init__({
            forms.TextInput(),
            forms.TextInput()
        }, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['', '']

class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name.')
            ]),
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid last name.')
            ]),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return f'{data_list[0]} {data_list[1]}'
"""
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(
            required=True,
            label='Username',
            widget=forms.TextInput(attrs={'placeholder':'Username'}),
            validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter valid username')
            ]
        )
        self.fields['first_name'] = forms.CharField(
            required=False,
            label='First Name',
            widget=forms.TextInput(attrs={'placeholder':'First Name'}),
            validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter valid first name')
            ]
        )
        self.fields['last_name'] = forms.CharField(
            required=False,
            label='Last Name',
            widget=forms.TextInput(attrs={'placeholder':'Last Name'}),
            validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter valid last name.')
            ]
        )
        self.fields['email'] = forms.CharField(
            required=True,
            label='Email',
            widget=forms.TextInput(attrs={'placeholder':'Email'}),
            validators=[
                RegexValidator(r'[a-zA-Z]+', message='Enter valid email')
            ]
        )

"""
    username = forms.CharField()
    name = NameField()
    email = forms.EmailField(label='E-Mail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'name',
            'email'
        )
"""
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'dob',
            'about_me',
            'image'
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'] = forms.DateField(
                            required=False,
                            input_formats=['%Y-%m-%d'],
                            label='Date of Birth',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder':'Date of Birth',
                                    'class':'form-control',
                            }),
                            )
        self.fields['about_me'] = forms.CharField(
                                required=False,
                                label='About Me',
                                widget=forms.Textarea(
                                    attrs={
                                        'placeholder':'Write something about yourself...',
                                        'rows':16,
                                        'cols':4,
                                        'class':'form-control',
                                        'style':'resize:none;'
                                    }),
                                )

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


"""
self.fields['username'] = forms.CharField(
    required=True,
    label='Username',
    widget=forms.TextInput(attrs={'placeholder':'Username'}),
    validators=[
        RegexValidator(r'[a-zA-Z]+', message='Enter valid username')
    ]
)
self.fields['first_name'] = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'placeholder':'First Name'}),
    validators=[
        RegexValidator(r'[a-zA-Z]+', message='Enter valid first name')
    ]
)
self.fields['last_name'] = forms.CharField(
    required=False,
    widget=forms.TextInput(attrs={'placeholder':'Last Name'}),
    validators=[
        RegexValidator(r'[a-zA-Z]+', message='Enter valid last name')
    ]
)
self.fields['email'] = forms.CharField(
    required=True,
    widget=forms.TextInput(attrs={'placeholder':'Email'}),
    validators=[
        RegexValidator(r'[a-zA-Z]+', message='Enter valid email')
    ]
)
"""
