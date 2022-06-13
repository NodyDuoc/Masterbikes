from django.db import models

# Create your models here.

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

