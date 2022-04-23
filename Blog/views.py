from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
from Blog.models import Post

# Create your views here.

@login_required
def blog(request):
      return render(request, "Blog/blog.html")

def posteo(request):
      if request.POST:
            posteo = Post()
            posteo.titulo = request.POST.get('titulo')
            posteo.subtitulo = request.POST.get('subtitulo')
            posteo.parrafo = request.POST.get('parrafo')
            posteo.autor = request.POST.get('autor')
            posteo.imagen = request.FILES.get('imagen')

            posteo.save()

            return render(request, "Base/pages/index.html")
      
      return render(request, "Blog/publicar.html")

def leerPosteos(request):

      posteos = Post.objects.all() #trae todos los profesores

      contexto= {"posteos":posteos} 

      return render(request, "Blog/blog.html",contexto)

def post(request, title):
      titulo = Post.objects.get(id=title)
      return render(request, "Blog/post.html")

      '''
      if request.method == 'POST':

            miFormulario = PostForm(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

            
                  informacion = miFormulario.cleaned_data

                  post = Post(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'],
                   parrafo=informacion['parrafo'], autor=informacion['autor']) 

                  post.save()

                  return render(request, "Base/pages/index.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PostForm() #Formulario vacio para construir el html

      return render(request, "Blog/publicar.html", {"miFormulario":miFormulario})
      '''