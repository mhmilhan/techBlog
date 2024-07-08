from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    mobile_number = forms.CharField(max_length=15, required=True, help_text='')
    image = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile_number', 'password1', 'password2', 'image')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Confirm Password'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Last Name'
        })
        self.fields['mobile_number'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Mobile Number'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secondary sm:text-sm',
            'placeholder': 'Profile Image'
        })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Password'
        })

