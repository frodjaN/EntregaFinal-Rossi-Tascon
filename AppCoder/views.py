from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    if request.method == 'POST':    #cuando le haga click al botón

        form = FormularioRegistro(request.POST)   #leer los datos   llenados en el formulario

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppCoder/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = FormularioRegistro()   #formulario de django que nos permite crear usuarios.
    
    
    return render(request, "AppCoder/Registro/registro.html", {'form':form})

def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "AppCoder/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppCoder/Registro/login.html", {'form':form})  

@login_required
def figus(request):

    figu = FiguYa.objects.all()


    return render(request, "AppCoder/VenderFigusYa/listaFigu.html",{'figuritas':figu})

def inicio(request):

    return render(request, "AppCoder/inicio.html")


def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioEquipo(request.POST)


        if formulario1.is_valid(): 

            info = formulario1.cleaned_data

            equipo = EquipoDeFutbol(nombre=info["nombre"], fechaNacimiento=info["fechaNacimiento"], pais=info["pais"], titulos=info["titulos"], mejorJugador=info["mejorJugador"]) 

            equipo.save() 

            return render(request, "AppCoder/inicio.html")

    else:
        formulario1=FormularioEquipo()


    return render(request, "AppCoder/formularioEquipo.html", {"formularioEquipo":formulario1}) 

def formulario2(request):

    if request.method=="POST":
        
        formulario2 = FormularioJugador(request.POST)


        if formulario2.is_valid(): 

            info = formulario2.cleaned_data

            jugador = JugadorFutbol(nombre=info["nombre"], nacionalidad=info["nacionalidad"], edad=info["edad"], posicion=info["posicion"], dorsal=info["dorsal"], piernaHabil=info["piernaHabil"])

            jugador.save() 

            return render(request, "AppCoder/inicio.html")

    else:
        formulario2=FormularioJugador() 


    return render(request, "AppCoder/formularioJugador.html", {"formularioJugador":formulario2}) 


def formulario3(request):

    if request.method=="POST":

        formulario3 = FormularioEstadio(request.POST)


        if formulario3.is_valid():

            info = formulario1.cleaned_data

            estadio = EstadioFutbol(nombre=info["nombre"], ubicacion=info["ubicacion"], fechaInauguracion=info["fechaInauguracion"], capacidad=info["capacidad"])

            estadio.save() 

            return render(request, "AppCoder/inicio.html") 

    else:
        formulario3=FormularioEstadio() 

    return render(request, "AppCoder/formularioEstadio.html", {"formularioEstadio":formulario3}) 



def busqueda(request):

    return render(request, "AppCoder/busqueda.html")

def busquedaEstadio(request):

    return render(request, "AppCoder/busquedaEstadio.html")

def busquedaEquipo(request):

    return render(request, "AppCoder/busquedaEquipo.html")
'''
def buscar(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        jugadores = JugadorFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultados.html", {"jugadores":jugadores, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)
'''
def buscarEquipo(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        equipos = EquipoDeFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultadosEquipo.html", {"equipos":equipos, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)

def buscarEstadio(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        estadios = EstadioFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultadosEstadio.html", {"estadios":estadios, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)

@login_required
def editarUsuario(request):

    usuario = request.user #usuario activo (el que ha iniciado sesión)

    if request.method == "POST":    #al presionar el botón

        miFormulario = FormularioRegistro(request.POST) #el formulario es el del usuario

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppCoder/Registro/inicio.html")

    else:

        miFormulario= FormularioRegistro(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppCoder/Registro/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})

@login_required
def agregarFiguYa(request):

    if request.method == 'POST':

        miFormulario=FiguYaFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            figu = FiguYa(nombre=informacion['nombre'], nacionalidad=informacion['nacionalidad'],
             posicion=informacion['posicion'], precio=informacion['precio'], reseña=informacion['reseña'],imagen=informacion['imagen'])

            figu.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario=FiguYaFormulario()

    return render(request, "AppCoder/VenderFigusYa/agregarFigu.html", {'form':miFormulario})

@login_required
def buscar(request):

    if request.GET["figurita"]:

        nombre=request.GET['figurita']

        resultados=FiguYa.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/VenderFigusYa/busquedaFigu.html",{"resultados":resultados, "busqueda":nombre})

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)

@login_required
def editarFigu(request, figurita_nombre):

    figu = FiguYa.objects.get(nombre=figurita_nombre)

    if request.method == "POST":

        miFormulario = FiguYaFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            figu.nombre = informacion['nombre']
            figu.nacionalidad = informacion['nacionalidad']
            figu.posicion = informacion['posicion']
            figu.precio = informacion['precio']
            figu.reseña = informacion['reseña']
            figu.imagen = informacion['imagen']

            figu.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario= FiguYaFormulario(initial={'nombre':figu.nombre, 'nacionalidad':figu.nacionalidad,
        'posicion':figu.posicion, 'precio':figu.precio, 'reseña':figu.reseña,'imagen':figu.imagen})

    return render(request, "AppCoder/VenderFigusYa/editarFigurita.html",{'miFormulario':miFormulario, 'figurita':figurita_nombre})
