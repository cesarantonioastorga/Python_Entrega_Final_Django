from django.db import models

# Create your models here.

class Signup(models.Model):
    usuario=models.CharField(max_length=30)
    correo=models.EmailField(max_length=50)
    contraseña=models.CharField(max_length=20)

    def __str__(self):
        return f"Usuario: {self.usuario} - Correo: {self.correo} - Contraseña: {self.contraseña}"