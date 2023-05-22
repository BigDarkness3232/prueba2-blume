from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TipoProducto(models.Model):
    nombreTipoProducto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreTipoProducto


class Producto(models.Model):
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    creado_en = models.DateField()
    modificado_en = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    imagen = models.ImageField(upload_to="mensajes", blank=True, null=True)
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 150)
    creado_en = models.DateField()
    modificado_en = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.nombre    

#class ProductoEspecial(models.Model):

class Carrito(models.Model):
    
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_carrito = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_prod = models.IntegerField(default=1)
    def __str__(self):
        return str(self.id_usuario)

class Orden(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_prod = models.IntegerField(default=1)
    total = models.IntegerField()
    def __str__(self):
        return str(self.id_usuario)