from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.blog, name="Pages"),
    path('publicar/', views.posteo, name='Posteo'),
    path('pages/', views.leerPosteos, name = "LeerPosteos"),
    path('post/<title>',views.post, name="Publicacion"),
]