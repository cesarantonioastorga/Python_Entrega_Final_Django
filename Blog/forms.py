from pyexpat import model
from django import forms
from .models import Post

'''
class SignupForm(forms.Form):
    usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese usuario'}),required=True)
    correo=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese correo electrónico'}),required=True)
    contraseña=forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese contraseña'}),required=True)
'''
class PostForm(forms.Form):
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Titulo'}),required=True)
    subtitulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Subtitulo'}),required=True)
    parrafo = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={"class":"form-control p-4", 'placeholder': 'Contenido'}),required=True)
    autor = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Autor'}),required=True)
    fecha = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control p-4"}))
    imagen = forms.ImageField()


