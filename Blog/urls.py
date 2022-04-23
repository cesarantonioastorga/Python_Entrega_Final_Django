from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.blog, name="Pages"),
    path('publicar/', views.posteo, name='Posteo')
]