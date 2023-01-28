from django import forms
from datetime import date
from .models import *


# Форма регистрации

class Registration(forms.Form):
    username = forms.CharField(label="Логин", max_length=10)  # Имя
    email = forms.EmailField(label='Email', initial='Ник или e-mail', required=True, help_text='(не обязательно)')
    password = forms.CharField(label='Пароль', initial='Пароль', widget=forms.PasswordInput)

class BbForm(forms.Form):
    pass