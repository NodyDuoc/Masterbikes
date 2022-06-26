from email import message
from tkinter.tix import Tree
from django.shortcuts import render, redirect
from .models import  Venta,RolUsuario, Usuario, Producto, Color, Categoria, TipoProducto, Carrito, Arriendo
from django.contrib import messages

# Create your views here.

def RegistrarArriendo(request):
    if request.POST:
        Fecha_Arriendo     = request.POST['fecha-arriendo']
        Fecha_Devolucion   = request.POST['fecha-devolucion'] 
        Categoria      = request.POST['Categoria']
        rut      = request.POST['rut']
        Arriendo.objects.create(FechaArriendo = Fecha_Arriendo, FechaDevolucion = Fecha_Devolucion, CategoriaBicicleta = Categoria,RutArrendador = rut)

        messages.success(request, 'Arriendo registrado')
        return redirect('arriendos')


def arriendos(request):
    return render(request,'Core/arriendos.html')

def RegistrarReparacion(request,id):
    sesi = Usuario.objects.get(idUsuario = id)
    contexto ={
        "sesion":sesi,
    }
    return render(request,'Core/RegistrarReparacion.html',contexto)

def RegistrarProducto(request,id):

    fotoProducto2          = request.FILES['fotoProducto']
    nombreProducto2       = request.POST['nombreProducto']
    precio2          = request.POST['precio']
    detalle2  = request.POST['detalle']
    Categoria2    = request.POST['Categoria']
    Color2     = request.POST['Color']

    Categoria3    = Categoria.objects.get(idCategoria = Categoria2)
    Color3         = Color.objects.get(idColor = Color2)


    Producto.objects.create(nombreProducto = nombreProducto2, fotoProducto = fotoProducto2, precio = precio2, detalle = detalle2, Categoria = Categoria3, Color = Color3)
    messages.success(request, 'Producto Registrado')
    return redirect ('ingresarProducto',id)
def ingresarProducto(request,id):
    sesi = Usuario.objects.get(idUsuario = id)
    cate = Categoria.objects.all()
    
    colo = Color.objects.all()
    contexto ={
        "sesion":sesi,
        "categoria":cate,
        "color":colo
    }
    return render(request,'Core/ingresarProducto.html',contexto)

def CarritoCompra(request,id):
    sesi    = Usuario.objects.get(idUsuario = id)
    carri   = Carrito.objects.all()
    product = Producto.objects.all()
    sum = 0
    if carri:
        for c in carri :
            if c.Usuario.idUsuario == sesi.idUsuario:
                sum = sum + c.Producto.precio
    contexto={
        "sesion":sesi,
        "carrito":carri,
        "productos": product,
        "sum":sum
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

def añadirCarrito(request,idUser,idProd):   
    User = Usuario.objects.get(idUsuario = idUser) 
    Prod = Producto.objects.get(idProducto = idProd)
    Carrito.objects.create(Usuario = User, Producto = Prod)
    return redirect ('detalleProdSesion',idUser,idProd)

def eliminarCarrito(request,idUser,idCarri):   
    carri = Carrito.objects.get(idCarrito = idCarri) 
    carri.delete()
    return redirect ('CarritoCompra',idUser)

def comprarCarrito(request,idUser):  
    User = Usuario.objects.get(idUsuario = idUser) 
 
    if Venta:
        numVentas = Venta.objects.all()
        max_value = None
        for num in numVentas:
            if (max_value is None or num.IdVenta > max_value):
                max_value = num.IdVenta
        maxVenta = max_value
    else:
        maxVenta = 1
    
    carri = Carrito.objects.all()
    for c in carri :
        if c.Usuario == User:
            Venta.objects.create(NumVenta = maxVenta, Usuario = User, Producto = c.Producto, Precio = c.Producto.precio)
            carr = Carrito.objects.get(idCarrito = c.idCarrito) 
            carr.delete()
    return redirect ('perfil',idUser)
  
    

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
    direccion2      = request.POST['direccion1']
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

        Usuario.objects.create(username = username2, nombre = nombre2, apellido = apellido2, email = email2, foto = foto2, contrasena = contrasena2, direccion = direccion2)
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
    direccion2  = request.POST['direccion1']
    

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
        usuario.nombre    = nombre2
        usuario.apellido  = apellido2
        usuario.email     = email2
        usuario.direccion = direccion2
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