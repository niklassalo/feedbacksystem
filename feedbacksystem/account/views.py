from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SignInView(LoginView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signin.html'