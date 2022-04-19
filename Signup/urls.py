from django.urls import path
from Signup import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/signup/', views.signupForm, name="SignupForm"),
]