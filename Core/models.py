from django.db import models

# Create your models here.
# Usuario
class RolUsuario(models.Model):
    idRol = models.AutoField(primary_key=True)
    nomRol = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) :
            return self.nomRol

class Usuario(models.Model):
    idUsuario  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=30, null=False)
    foto = models.ImageField(upload_to="foto_perfil", default="foto_perfil/foto_perfil_default.png", blank='')
    contrasena = models.CharField(max_length=20, null=False, blank=False)
    RolUsuario = models.ForeignKey(RolUsuario, on_delete= models.CASCADE, default=1)

    def __str__(self) :
            return self.username
# Producto
class TipoProducto(models.Model):
    idTipo = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=60, null=False, blank=False)
    def __str__(self) :
            return self.nombreTipo
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=60, null=False, blank=False)
    TipoProducto = models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    def __str__(self) :
            return self.nombreCategoria
class Color(models.Model):
    idColor = models.AutoField(primary_key=True)
    nombreColor = models.CharField(max_length=60, null=False, blank=False)
    def __str__(self) :
            return self.nombreColor

class Producto(models.Model):
    idProducto     = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=60, null=False, blank=False)
    fotoProducto   = models.ImageField(upload_to="foto_perfil", default="foto_perfil/foto_perfil_default.png", blank='')
    detalle        = models.CharField(max_length=60, null=False, blank=False)
    Categoria      = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    Color          = models.ForeignKey(Color, on_delete= models.CASCADE)
    def __str__(self) :
            return self.nombreProducto
