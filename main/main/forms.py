from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

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
            'class': 'block w-full px-3 py-2 border border-primary rounded-md shadow-sm placeholder-accent focus:outline-none focus:ring-secondary focus:border-secodary sm:text-sm',
            'placeholder': 'Confirm Password'
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