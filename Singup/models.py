from django.db import models

# Create your models here.

class Singup(models.Model):
    usuario=models.CharField(max_length=30)
    correo=models.EmailField(max_length=50)
    contraseña=models.CharField(max_length=20)