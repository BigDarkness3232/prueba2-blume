from django.urls import path
from .views import *


urlpatterns = [
    	path('', index, name="index"),
        # Productos
        path('productos/arbustos/', arbustos, name="arbustos"),
		path('productos/flores/', flores, name="flores"),
        path('productos/herramientas/', herramientas, name="herramientas"),
        path('productos/macetas/', macetas, name="macetas"),
        path('productos/sustratos/', sustratos, name="sustratos"),
        # Pagos
        path('subscripcion/', subscripcion, name="subscripcion"),
        # CRUD
        path('agregar/', agregar, name="agregar"),
        path('modificar/<id>/', modificar, name="modificar"),
        path('eliminar/<id>/', eliminar, name="eliminar"),
        # Administracion
        path('menuadmin/', menuadmin , name="menuadmin"),
        #Carrito
        path('carrito/', carrito, name="carrito"),
        path('car_agregar/<id>/', car_agregar, name="carrito_agregar"),
        path('car_eliminar/<id>/', car_eliminar, name="carrito_eliminar"),
        path('car_eliminartodo/', car_eliminar_todo, name="carrito_borra_todo"),
        #Perfil
        path('perfil/', perfil, name="perfil"),
        #Pedidos
        path('pedidos/', pedidos, name="pedidos"),
        # CRUD Mensajes
        path('agregarm/', agregarm, name="agregarm"),
        path('modificarm/<id>/', modificarm, name="modificarm"),
        path('eliminarm/<id>/', eliminarm, name="eliminarm"),
        #menumensajes
        path('menumensajes/', menumensajes, name="menumensajes"),
]
