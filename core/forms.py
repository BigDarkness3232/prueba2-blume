from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=4,widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    marca = forms.CharField(min_length=4,widget=forms.TextInput(attrs={"placeholder":"Ingrese Marca"}))
    descripcion = forms.CharField(min_length=10,max_length=200,widget=forms.Textarea(attrs={"rows":4}))
    precio = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Stock"}))
    
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'creado_en' : forms.SelectDateWidget(years=range(2020,2030)),
            'modificado_en' : forms.SelectDateWidget(years=range(2020,2030))
        }


class MensajeForm(ModelForm):

    nombre = forms.CharField(min_length=4,widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre del mensaje"}))
    descripcion = forms.CharField(min_length=10,max_length=200,widget=forms.Textarea(attrs={"rows":4}))


    class Meta:
        model = Mensaje
        fields = '__all__'
        widgets = {
            'creado_en' : forms.SelectDateWidget(years=range(2020,2030)),
            'modificado_en' : forms.SelectDateWidget(years=range(2020,2030))
        }