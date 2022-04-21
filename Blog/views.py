from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
from Blog.models import Post

# Create your views here.

@login_required
def blog(request):
      return render(request, "Blog/blog.html")

def posteo(request):

      if request.method == 'POST':

            miFormulario = PostForm(data=request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  titulo=request.POST.get('titulo')
                  subtitulo=request.POST.get('subtitulo')
                  parrafo=request.POST.get('parrafo')
                  autor=request.POST.get('autor')
                  fecha=request.POST.get('fecha')
                  imagen=request.POST.get('imagen')
                  '''
                  #informacion = miFormulario.cleaned_data
                  
                  post = Post(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'],
                   parrafo=informacion['parrafo'], autor=informacion['autor'], fecha=informacion['fecha'], imagen=informacion['imagen']) 
             
                  #post.save()
                   '''
                  return render(request, "Base/pages/index.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PostForm() #Formulario vacio para construir el html

      return render(request, "Blog/publicar.html", {"miFormulario":miFormulario})
     