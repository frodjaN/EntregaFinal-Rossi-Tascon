from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('figuYa', views.figus, name='Figus'),
    path("buscar/", buscar, name="buscar2"),
    path('accounts/login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/Registro/logout.html'), name='Logout'),
    path('accounts/signup', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="Editar Usuario"),
    path('agregarFigu', views.agregarFiguYa, name='Agregar FiguYa'),
    path("editarFigurita/<figurita_nombre>", views.editarFigu, name="Editar Figu"),
    path('agregarAvatar/', views.agregarAvatar, name='AgregarAvatar'),
]