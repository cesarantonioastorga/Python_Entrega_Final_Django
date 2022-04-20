from django.shortcuts import render
from Login.forms import LoginForm

# Create your views here.

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



def login_request(request):

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

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

    form = LoginForm()

    return render(request, "Login/login.html", {"form": form})
