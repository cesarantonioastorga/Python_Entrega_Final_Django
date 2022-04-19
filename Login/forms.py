from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese usuario'}),required=True)
    contraseña=forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese contraseña'}),required=True)