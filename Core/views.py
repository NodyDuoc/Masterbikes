from email import message
from tkinter.tix import Tree
from django.shortcuts import render, redirect
from .models import RolUsuario, Usuario, Producto, Color, Categoria, TipoProducto, Carrito
from django.contrib import messages

# Create your views here.

def CarritoCompra(request,id):
    sesi    = Usuario.objects.get(idUsuario = id)
    carri   = Carrito.objects.all()
    product = Producto.objects.all()
    contexto={
        "sesion":sesi,
        "carrito":carri,
        "productos": product
    }
    return render(request,'Core/CarritoCompra.html',contexto)

def index(request):
    return render(request,'Core/index.html')
def catalogo(request):
    product = Producto.objects.all()
    contexto={
        "productos": product
    }
    return render(request,'Core/catalogo.html',contexto)
def catalogoSesion(request,id):
    sesi = Usuario.objects.get(idUsuario = id)
    product = Producto.objects.all()
    contexto={
        "sesion":sesi,
        "productos": product
    }
    return render(request,'Core/catalogoSesion.html',contexto)

def detalleProdSesion(request,idUser,idProd):
    sesi = Usuario.objects.get(idUsuario = idUser)
    prod      = Producto.objects.get(idProducto = idProd)
    catego    = Categoria.objects.get(idCategoria = prod.Categoria.idCategoria)
    tipo      = TipoProducto.objects.get(idTipo = catego.TipoProducto.idTipo)

    contexto={
        "sesion":sesi,
        "prod": prod,
        "catego": catego,
        "tipo" : tipo,
    }
    return render(request,'Core/detalleProdSesion.html',contexto)

def añadirCarrito(request,idDser,idProd):   
    cantidad2 = request.POST['cantidad1']
    User = Usuario.objects.get(idUsuario = idDser) 
    Prod = Producto.objects.get(idProducto = idProd)
    Carrito.objects.create(Usuario = User, Producto = Prod, Cantidad = cantidad2)
    return redirect ('detalleProd',idProd)
    

def detalleProd(request,id):
    prod      = Producto.objects.get(idProducto = id)
    catego    = Categoria.objects.get(idCategoria = prod.Categoria.idCategoria)
    tipo      = TipoProducto.objects.get(idTipo = catego.TipoProducto.idTipo)

    contexto={
        "prod": prod,
        "catego": catego,
        "tipo" : tipo,
    }
    return render(request,'Core/detalleProd.html',contexto)

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
def modFotoUser(request,id):
    contexto = {
        "sesion":Usuario.objects.get(idUsuario = id)
    }
    return render(request,'Core/modFotoUser.html',contexto)
    

def userFotoModificado(request,id):

    x = Usuario.objects.get(idUsuario = id)
 
    foto2 = request.FILES['foto1']
    x.foto = foto2
    x.save() #update
    messages.success(request, 'Foto Modificada')
    contexto ={
        "sesion":x
        }
    return redirect ('perfil',x.idUsuario)
        
  

def modDatosUser(request,id):
    contexto = {
        "sesion":Usuario.objects.get(idUsuario = id)
    }
    return render(request,'Core/modDatosUser.html',contexto)




def userDatosModificado(request,id):
    usuario           = Usuario.objects.get(idUsuario = id)
    
    username2   = request.POST['username1']
    nombre2     = request.POST['nombre1']
    apellido2   = request.POST['apellido1']
    email2      = request.POST['email1']

    try:
        c = Usuario.objects.get(email = email2)
        if id == c.idUsuario:
            c1 = True
        else:
            c1 = False
    except Usuario.DoesNotExist:
        c1 = True
    try:
        x = Usuario.objects.get(username = username2)
        if id == x.idUsuario:
            x1 = True
        else:
            x1 = False
    except Usuario.DoesNotExist:
        x1 = True


    if c1 == True and x1 == True:
        messages.error(request, 'Perfil modificado')
        usuario.username = username2
        usuario.nombre = nombre2
        usuario.apellido = apellido2
        usuario.email = email2
        usuario.save() #update
        contexto ={
        "sesion":usuario
        }
        return redirect ('perfil',usuario.idUsuario)
    else:
        messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        contexto ={
        "sesion":usuario
        }
        return redirect ('perfil',usuario.idUsuario)