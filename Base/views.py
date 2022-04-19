from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request, "Base/pages/index.html")

def noticias(request):
      return render(request, "Base/pages/pages.html")

def tienda(request):
      return render(request, "Base/pages/tienda.html")

def nosotros(request):
      return render(request, "Base/pages/about.html")

def contacto(request):
      return render(request, "Base/pages/contacto.html")

def ingresar(request):
      return render(request, "Base/pages/ingresar.html")

def registro(request):
      return render(request, "Base/pages/registro.html")

def perfil(request):
      return render(request, "Base/pages/profile.html")