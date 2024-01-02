from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    UsernameField,
)

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Введите имя пользователя",
            }
        )
    )

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )

    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поддтвердите ваш пароль",
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "photo",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    photo = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()


# class ProfileForm(UserChangeForm):
#
#     image = forms.ImageField(
#         widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
#     )
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите ваше имя",
#             }
#         )
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите вашу фамилию",
#             }
#         )
#     )
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите ваше имя пользователя",
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите ваш email *youremail@example.com",
#                 # 'readonly': True,
#             }
#         ),
#     )
#
#     class Meta:
#         model = User
#         fields = (
#             "image",
#             "first_name",
#             "last_name",
#             "username",
#             "email",)
