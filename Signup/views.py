from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Signup.forms import SignupForm, UserEditForm

# Create your views here.


def signupForm(request):

    if request.method == "POST":
        # Aqui me llega la informacion del html
        registroFormulario = UserCreationForm(request.POST)
        registroFormulario = SignupForm(request.POST)
        print(registroFormulario)

        if registroFormulario.is_valid():
            username = registroFormulario.cleaned_data['username']
            registroFormulario.save()
        return render(request, "Base/pages/index.html", {"Mensaje":"Usuario creado"})
    else:
        registroFormulario = UserCreationForm()
        registroFormulario = SignupForm()

    return render(request, "Signup/registro.html", {"registroFormulario": registroFormulario})

# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        registroFormulario = UserEditForm(request.POST)
        if registroFormulario.is_valid():
            informacion = registroFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "Base/pages/index.html")
    else:
        registroFormulario = UserEditForm(initial={'email': usuario.email})
        
    return render(request, "Signup/editar_perfil.html", {"registroFormulario": registroFormulario, "usuario": usuario})

@login_required
def perfil(request):
      return render(request, "Signup/profile.html")

'''
def signupForm(request):

    if request.method == "POST":
        # Aqui me llega la informacion del html
        registroFormulario = SignupForm(request.POST)
        print(registroFormulario)

        if registroFormulario.is_valid:
            informacion = registroFormulario.cleaned_data
            registro = Signup(
                usuario=informacion["usuario"], correo=informacion["correo"], contraseña=informacion["contraseña"])
            registro.save()
        return render(request, "Base/pages/index.html")
    else:
        registroFormulario = SignupForm()

    return render(request, "Signup/registro.html", {"registroFormulario": registroFormulario})
'''