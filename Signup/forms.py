from django import forms


class SignupForm(forms.Form):
    usuario=forms.CharField(max_length=30)
    correo=forms.EmailField(max_length=50)
    contraseña=forms.CharField(max_length=20)