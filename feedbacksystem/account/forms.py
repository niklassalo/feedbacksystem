from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class': 'form-control'})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})