#encoding: utf-8
from django import forms
from django.contrib.auth.models import User

attrs_dict = { 'class': 'required' }

class LoginForm(forms.Form):
    
    username = forms.CharField( max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label='Usuario')

    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label='Senha')

class CadastroForm(forms.Form):
    username = forms.CharField( max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label='Usuario')
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label='Email')
    first_name = forms.CharField(max_length=60, label="Primeiro Nome")
    last_name = forms.CharField(max_length=60, label="Ultimo Nome")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label='Confirmar Senha')
