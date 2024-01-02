from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, TemplateView

from users.forms import LoginForm, ProfileForm, RegistrationForm


@method_decorator(login_required, name="dispatch")
class ProfilePage(View):
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ProfileForm(instance=request.user)
            context = {"form": form}
            return render(request, template_name=self.template_name, context=context)
        # else:
        #     return redirect("users:login")

    def post(self, request, *args, **kwargs):
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            context = {
                "form": form,
            }
            return render(request, template_name=self.template_name, context=context)


class LoginPage(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        messages.success(self.request, f"Добро пожаловть!")
        return super().form_valid(form)


class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        logout(request)
        messages.warning(request, f"{username} вы вышли из аккаунта")
        return redirect(reverse("users:login"))


class RegistrationPage(FormView):
    template_name = "users/registration.html"
    form_class = RegistrationForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(
            self.request,
            f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт",
        )

        return super().form_valid(form)


class CartPage(TemplateView):
    template_name = "users/cart.html"
