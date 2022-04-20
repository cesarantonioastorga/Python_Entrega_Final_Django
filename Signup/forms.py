from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''
class SignupForm(forms.Form):
    usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese usuario'}),required=True)
    correo=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese correo electrónico'}),required=True)
    contraseña=forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese contraseña'}),required=True)
'''
class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese usuario'}),required=True)
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese correo electrónico'}),required=True)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese contraseña'}),required=True)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Repetir contraseña'}),required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
