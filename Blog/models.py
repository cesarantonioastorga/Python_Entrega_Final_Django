from django.db import models

# Create your models here.

'''
class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null=False,blank=False)
    estado = models.BooleanField('Categoria activada / Categoria Desactivada', default=True)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres=models.CharField('Nombres de autor', max_length=255, null=False, blank=False)
    apellidos=models.CharField('Apellidos de autor', max_length=255, null=False,blank=False)
    facebook=models.URLField('Facebook', null = True, blank=True)
    twitter=models.URLField('Twitter', null = True, blank=True)
    instagram=models.URLField('Instagram', null = True, blank=True)
    youtube=models.URLField('Youtube', null = True, blank=True)
    web=models.URLField('Web', null=True,blank=True)
    correo=models.EmailField('Correo Electronico', blank=False, null=False)
    estado=models.BooleanField('Autor Activo/Inactivo', default=True)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

'''
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    parrafo = models.CharField(max_length=2000)
    autor = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True, auto_now=False)
    imagen = models.ImageField(null = True, blank=True, upload_to='imagenes/')
