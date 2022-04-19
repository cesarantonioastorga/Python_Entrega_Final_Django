from django import forms


class SignupForm(forms.Form):
    usuario=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese usuario'}),required=True)
    correo=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese correo electrónico'}),required=True)
    contraseña=forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={"class":"form-control p-4", 'placeholder': 'Ingrese contraseña'}),required=True)