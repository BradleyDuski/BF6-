from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView 
from django.contrib.auth.models import User
from .forms import SignupForm


class UserLogin(LoginView):
    template_name = "users/login.html"


class UserSignup(CreateView):
    model = User
    form_class = SignupForm
    template_name = "users/signup.html"
    success_url = '/users/login'

    def form_valid(self, form):
        user = form.save(commit=False)
        pass_text = form.cleaned_data["password"]
        user.set_password(pass_text)
        user.save()

        return super().form_valid(form)