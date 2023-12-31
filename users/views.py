from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView

from users.forms import LoginForm


class ProfilePage(TemplateView):
    template_name = "users/profile.html"


class LoginPage(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    # success_url = reverse_lazy('main:main_page')


class LogoutPage(LogoutView):
    pass


class RegistrationPage(TemplateView):
    template_name = "users/registration.html"
