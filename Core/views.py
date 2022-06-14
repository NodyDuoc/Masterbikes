from email import message
from tkinter.tix import Tree
from django.shortcuts import render, redirect
from .models import RolUsuario, Usuario
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Core/index.html')
def login(request):
    return render(request,'Core/login.html')
def registro(request):
    return render(request,'Core/registro.html')
def registrarUsuario(request):
    username2   = request.POST['username1']
    nombre2     = request.POST['nombre1']
    apellido2   = request.POST['apellido1']
    email2      = request.POST['email1']
    contrasena2 = request.POST['contrasena1']
    foto2       = request.FILES['foto1']
    try:
        c = Usuario.objects.get(email = email2)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      
    try:
        x = Usuario.objects.get(username = username2)
        x1 = False
    except Usuario.DoesNotExist:
        x1 = True
    if c1 == True and x1 == True:

        Usuario.objects.create(username = username2, nombre = nombre2, apellido = apellido2, email = email2, foto = foto2, contrasena = contrasena2)
        sesion = Usuario.objects.get(username = username2)
        contexto ={
        "sesion":sesion
        }
        messages.success(request, 'Cuenta registrada')
        return redirect ('registro')
    else:
        messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect ('registro')


def loginUser(request):
    us = request.POST['username1']
    cl = request.POST['contrasena1']
    try:
        x = Usuario.objects.get(username = us, contrasena = cl)
        
        contexto ={
        "sesion":x
        }
        return redirect ('perfil',x.idUsuario)

    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario y/o clave incorrecta')
        return redirect ('login')

def perfil(request,id):
    contexto ={
        "sesion":Usuario.objects.get(idUsuario = id)
        }
    return render(request,'Core/perfil.html',contexto)
