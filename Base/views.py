from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Avatar

# Create your views here.

def index(request):
      return render(request, "Base/pages/index.html")

@login_required
def noticias(request):
      return render(request, "Base/pages/pages.html")

@login_required
def tienda(request):
      return render(request, "Base/pages/tienda.html")

@login_required
def nosotros(request):
      return render(request, "Base/pages/about.html")

@login_required
def contacto(request):
      return render(request, "Base/pages/contacto.html")

@login_required
def perfil(request):
      return render(request, "Base/pages/profile.html")
