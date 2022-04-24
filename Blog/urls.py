from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.blog, name="Pages"),
    path('publicar/', views.posteo, name='Posteo'),
    path('pages/', views.leerPosteos, name = "LeerPosteos"),
    path('post/<title>',views.post, name="Publicacion"),
    path(r'^editar/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PostDelete.as_view(), name='Delete'),
]