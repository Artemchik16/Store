from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя',
    }))

    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': 'form-control',
            'placeholder': 'Введите пароль',
        }),
    )

    class Meta:
        model = User
