from django.contrib import admin
from .models import *

# Register your models here.

class TipoProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ['id', 'nombreTipoProducto']

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ['nombre', 'marca', 'descripcion', 'precio', 'stock', 'tipo', 'creado_en', 'modificado_en', 'imagen']
    list_editable = ['marca', 'descripcion', 'precio', 'stock', 'tipo', 'creado_en', 'modificado_en', 'imagen']

    list_per_page = 10
    search_fields = ['nombre']
    list_filter = ['tipo']

class CarritoAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ['id_usuario', 'producto_carrito','cantidad_prod']
    list_editable = ['producto_carrito','cantidad_prod']

class MensajeAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = [ 'nombre','descripcion', 'imagen']
    list_editable = [ 'descripcion', 'imagen']

    list_per_page = 10


admin.site.register(TipoProducto, TipoProductoAdmin )
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Producto, ProductoAdmin )
admin.site.register(Carrito, CarritoAdmin)



#<!-- {% if user.username == 'admin' %} -->

