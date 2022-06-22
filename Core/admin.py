from django.contrib import admin
from .models import Venta ,RolUsuario, Usuario, TipoProducto, Categoria, Color, Producto, Carrito
# Register your models here.
admin.site.register(RolUsuario)
admin.site.register(Usuario)
admin.site.register(TipoProducto)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Venta)
