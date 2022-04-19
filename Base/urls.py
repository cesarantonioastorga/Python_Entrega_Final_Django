from django.urls import path, include
from Base import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name="Inicio"),
    path('pages/', views.noticias, name="Noticias"),
    path('tienda/', views.tienda, name="Tienda"),
    path('about/', views.nosotros, name="Nosotros"),
    path('contacto/', views.contacto, name="Contacto"),
    path('accounts/profile/', views.perfil, name="Perfil"),
]