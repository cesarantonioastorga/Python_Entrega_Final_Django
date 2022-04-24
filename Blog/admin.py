from django.db import models
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)


'''
class CategoriaAdmin(admin.ModelAdmin):
    search_function=['nombre']
    list_display=('nombre', 'estado', 'fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_function=['nombres','apellidos','correo']
    list_display=('nombres','apellidos','correo','estado','fecha_creacion',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
'''