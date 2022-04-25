from django.urls import path
from Signup import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.signupForm, name="SignupForm"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('profile/', views.perfil, name="Perfil"),
]