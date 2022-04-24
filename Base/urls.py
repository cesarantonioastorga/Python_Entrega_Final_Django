from django.urls import path, include
from Base import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Inicio"),
    path('noticias/', views.noticias, name="Noticias"),
    path('tienda/', views.tienda, name="Tienda"),
    path('about/', views.nosotros, name="Nosotros"),
    path('contacto/', views.contacto, name="Contacto"),
    path('accounts/profile/', views.perfil, name="Perfil"),
    path('', RedirectView.as_view(url='/Base/', permanent=True)), # Para que ingrese directamente a nuestra pagina
]

#Clase 24 --> Para las imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)