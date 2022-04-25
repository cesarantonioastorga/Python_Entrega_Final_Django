from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
from Blog.models import Post

# Create your views here.

@login_required
def blog(request):
      return render(request, "Blog/blog.html")

@login_required
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

@login_required
def leerPosteos(request):

      posteos = Post.objects.all() #trae todos los profesores

      contexto= {"posteos":posteos} 

      return render(request, "Blog/blog.html",contexto)

@login_required
def post(request, title):
      id_post = Post.objects.get(id=title)
      '''
      subtitulo = request.POST.get('subtitulo')
      parrafo = request.POST.get('parrafo')
      autor = request.POST.get('autor')
      imagen = request.FILES.get('imagen')
      '''
      return render(request, "Blog/post.html",{'detalle':id_post})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostUpdate(UpdateView):

    model = Post
    success_url = "/Inicio/pages"
    fields = ['titulo', 'subtitulo', 'parrafo', 'autor', 'imagen']

class PostDelete(DeleteView):

    model = Post
    success_url = "/Inicio/pages"

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