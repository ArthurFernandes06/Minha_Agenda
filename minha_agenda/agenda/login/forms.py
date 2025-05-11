# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Usuário"))
    password = forms.CharField(label=_("Senha"), widget=forms.PasswordInput)
