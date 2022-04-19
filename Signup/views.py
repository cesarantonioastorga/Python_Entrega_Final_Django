from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Signup.forms import SignupForm
from Signup.models import Signup

# Create your views here.


def SignupForm(request):

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

    return render(request, "Base/pages/registro.html", {"registroFormulario": registroFormulario})

