from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", register, name="register"),
    path("login/", LoginView.as_view(template_name="main/login.html"), name="login"),
    path("home/", home_page, name="home"),
    path("logout/", LogoutView.as_view(template_name="main/logout.html"), name="logout")
]