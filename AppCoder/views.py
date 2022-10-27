from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from AppCoder.forms import *
from AppCoder.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def register(request):

    if request.method == 'POST':   

        form = FormularioRegistro(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppCoder/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = FormularioRegistro()   
    
    
    return render(request, "AppCoder/Registro/registro.html", {'form':form})

def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)   

            if user:    

                login(request, user)   

                
                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   

            
    
            return render(request, "AppCoder/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "AppCoder/Registro/login.html", {'form':form})  

@login_required
def agregarAvatar(request):
    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = Avatar (user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = AvatarFormulario()

    return render(request, "AppCoder/Registro/agregarAvatar.html", {"miFormulario":miFormulario})
    

def figus(request):

    figu = FiguYa.objects.all()


    return render(request, "AppCoder/VenderFigusYa/listaFigu.html",{'figuritas':figu})


def inicio(request):



    return render(request, "AppCoder/inicio.html")



@login_required
def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        miFormulario = FormularioRegistro(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     

            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.bio = informacion['bio']
            usuario.imagen = informacion['imagen']
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


def buscar(request):

    if request.GET["figurita"]:

        nombre=request.GET['figurita']

        resultados=FiguYa.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/VenderFigusYa/busquedaFigu.html",{"resultados":resultados, "busqueda":nombre})

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)

@staff_member_required
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


@staff_member_required
def borrarFigu(request, figurita_nombre):

    figuritaz = FiguYa.objects.get(nombre=figurita_nombre)
    
    figuritaz.delete()
    
    figuritas = FiguYa.objects.all()

    return render(request, "AppCoder/VenderFigusYa/listaFigu.html",{'figuritas':figuritas})


@login_required
def comprarFiguYa(request):

    if request.method == 'POST':

        miFormulario=CompraFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            oferta = CompraFigu(oferta=informacion['oferta'],)

            oferta.save()

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario=CompraFormulario()

    return render(request, "AppCoder/VenderFigusYa/compraFigu.html", {'form':miFormulario})

def aboutUs(request):
    
    return render(request, "AppCoder/aboutUs.html")