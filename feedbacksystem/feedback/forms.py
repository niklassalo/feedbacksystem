from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'grade', 'good', 'bad', 'ideas']
        # widgets = {
        #     'good': forms.Textarea(attrs={'rows': 3}),
        #     'bad': forms.Textarea(attrs={'rows': 3}),
        #     'ideas': forms.Textarea(attrs={'rows': 3}),
        # }

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))