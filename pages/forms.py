from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={
        "class": "form-control bg-dark text-danger"
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control bg-dark text-danger"
    }))

    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control bg-dark text-danger"
    }))

    password2 = forms.CharField(label="Повторите Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control bg-dark text-danger"
    }))

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control bg-dark text-danger"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control bg-dark text-danger"
            })
        }