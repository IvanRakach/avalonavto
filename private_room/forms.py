from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-control-register',
                                                             "placeholder": "Введите логин"}))  # form-input // "style": "width: 200px float: left"
    phone_number = forms.CharField(label="Номер телефона",
                                   widget=forms.TextInput(attrs={'class': 'form-control-register',
                                                                 "placeholder": "Введите номер телефона"}))  # "style": "width: 200px",
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control-register',
                                                            "placeholder": "Введите email"}))  # "style": "width: 200px",
    password1 = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(attrs={'class': 'form-control-register',
                                                                  "placeholder": "Введите пароль"}))  # "style": "width: 200px",
    password2 = forms.CharField(label="Повтор пароля",
                                widget=forms.PasswordInput(attrs={'class': 'form-control-register',
                                                                  "placeholder": "Подтвердите пароль"}))  # "style": "width: 200px",

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUSerForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control-login',
                                                                            "placeholder": "Введите логин"}))  # form-input
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control-login',
                                                                                 "placeholder": "Введите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'password')
