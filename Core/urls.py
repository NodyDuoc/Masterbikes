"""MasterBikes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.urls import URLPattern, path
from django.conf import settings
from .views import eliminarCarrito, añadirCarrito,CarritoCompra, detalleProdSesion, catalogoSesion, index, login, perfil, registro, registrarUsuario,loginUser, modFotoUser, userFotoModificado,modDatosUser,userDatosModificado, catalogo, detalleProd
from . import views
from .models import RolUsuario, Usuario
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('eliminarCarrito/<idUser>/<idCarri>',eliminarCarrito,name="eliminarCarrito"),
    path('añadirCarrito/<idUser>/<idProd>',añadirCarrito,name="añadirCarrito"),
    path('CarritoCompra/<int:id>',CarritoCompra,name="CarritoCompra"),
    path('detalleProdSesion/<idUser>/<idProd>',detalleProdSesion,name="detalleProdSesion"),
    path('catalogoSesion/<int:id>',catalogoSesion,name="catalogoSesion"),
    path('',index,name="index"),
    path('login/',login,name="login"),
    path('perfil/<int:id>',perfil,name="perfil"),
    path('registro/',registro,name="registro"),
    path('registrado/',registrarUsuario,name="registrarUsuario"),
    path('loginUser/',loginUser,name="loginUser"),
    path('perfil/<int:id>',perfil,name="perfil"),
    path('modFotoUser/<int:id>',modFotoUser,name="modFotoUser"),
    path('userFotoModificado/<int:id>',userFotoModificado,name="userFotoModificado"),
    path('modDatosUser/<int:id>',modDatosUser,name="modDatosUser"),
    path('userDatosModificado/<int:id>',userDatosModificado,name="userDatosModificado"),
    path('catalogo/',catalogo,name="catalogo"),
    path('detalleProd/<int:id>',detalleProd,name="detalleProd"),
]   

