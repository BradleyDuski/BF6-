from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView 
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import logout


class UserLogin(LoginView):
    template_name = "users/login.html"

def logout_view(request):
    logout(request)
    return redirect('login')  

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