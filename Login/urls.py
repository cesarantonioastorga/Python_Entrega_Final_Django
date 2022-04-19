from django.urls import path, include
from Login import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/login/', views.login_request, name="Login"),
]


