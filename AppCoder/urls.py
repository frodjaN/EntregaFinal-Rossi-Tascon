from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('figuYa', views.figus, name='Figus'),
    path("equipo/", formulario1, name="form1"),
    path("jugador/", formulario2, name="form2"),
    path("estadio/", formulario3, name="form3"),
    path("busqueda/", busqueda, name="Buscar"),
    path("busquedaEquipo/", busquedaEquipo, name="BuscarEquipo"),
    path("busquedaEstadio/", busquedaEstadio, name="BuscarEstadio"),
    path("buscar/", buscar, name="buscar2"),
    path("buscarEquipo/", buscarEquipo),
    path("buscarEstadio/", buscarEstadio),
    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/Registro/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="Editar Usuario"),
    path('agregarFigu', views.agregarFiguYa, name='Agregar FiguYa'),
    path("editarFigurita/<figurita_nombre>", views.editarFigu, name="Editar Figu"),
]