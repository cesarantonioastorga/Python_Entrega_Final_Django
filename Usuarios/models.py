from django.db import models
# Create your models here.

class Usuario(models.Model):
    imagen = models.ImageField(null = True, blank=True, upload_to='imagenes/')    
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField(max_length=100)
    web=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    contraseña=models.CharField(max_length=20)
