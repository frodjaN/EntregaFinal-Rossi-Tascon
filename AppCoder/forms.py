from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import *

class FormularioEquipo(forms.Form):

    nombre = forms.CharField()
    fechaNacimiento = forms.DateField()
    pais = forms.CharField()
    titulos = forms.IntegerField()
    mejorJugador = forms.CharField()

class FormularioJugador(forms.Form):

    nombre = forms.CharField()
    nacionalidad = forms.CharField()
    edad = forms.IntegerField()
    posicion = forms.CharField()
    dorsal = forms.IntegerField()
    piernaHabil = forms.CharField()

class FormularioEstadio(forms.Form):

    nombre = forms.CharField()
    ubicacion = forms.CharField()
    fechaInauguracion = forms.DateField()
    capacidad = forms.IntegerField()

class FormularioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class FiguYaFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    nacionalidad= forms.CharField(max_length=40)
    posicion= forms.CharField(max_length=40)
    precio= forms.IntegerField()
    reseña= forms.CharField(widget=forms.Textarea)
    imagen= forms.ImageField()

class FiguYaVender(forms.Form):

    class Meta:

        model = FiguYa
        fields = ['nombre', 'nacionalidad', 'posicion', 'precio', 'reseña', 'imagen']
