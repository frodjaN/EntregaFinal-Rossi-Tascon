from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EquipoDeFutbol(models.Model):

    nombre = models.CharField(max_length=60)
    fechaNacimiento = models.DateField()
    pais = models.CharField(max_length=60)
    titulos = models.PositiveIntegerField(default=0)
    mejorJugador = models.CharField(max_length=60)

class JugadorFutbol(models.Model):
    nombre = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    edad = models.PositiveIntegerField(default=0)
    posicion = models.CharField(max_length=60)
    dorsal = models.PositiveIntegerField(default=0)
    piernaHabil = models.CharField(max_length=60)

class EstadioFutbol(models.Model):
    nombre = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=60)
    fechaInauguracion = models.DateField()
    capacidad = models.PositiveIntegerField(default=0)

class FiguYa(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    precio = models.IntegerField()
    reseña = models.TextField(max_length=240)
    imagen = models.ImageField(upload_to = 'figuritas', null=True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank=True)

    class Meta:
        verbose_name= "Avatar"
        verbose_name_plural= "Avatares"
