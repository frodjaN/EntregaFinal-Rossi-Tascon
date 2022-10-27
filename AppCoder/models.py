from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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

class CompraFigu(models.Model):
    oferta = models.TextField(max_length=240)
