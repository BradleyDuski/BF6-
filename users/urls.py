from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("login/", views.UserLogin.as_view(), name='login'),
path("signup/", views.UserSignup.as_view(), name="signup"),
path("logout/", views.logout_view, name='logout')
]