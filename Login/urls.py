from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
#from Login import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='Login/login.html'), name='Login'),
    path('logout/', logout_then_login, name='Logout'),
]


