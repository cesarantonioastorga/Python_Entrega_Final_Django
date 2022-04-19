from django.shortcuts import render
from Signup.forms import SignupForm
from Signup.models import Signup

# Create your views here.

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('usuario')
            contraseña = form.cleaned_data.get('contraseña')

            user = authenticate(usuario= usuario, contraseña=contraseña)

            if user is not None:
                login(request, user)

                return render(request, "Base/pages/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Base/pages/index.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Base/pages/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Login/login.html", {"form": form})