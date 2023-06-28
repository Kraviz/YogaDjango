

from django import forms
from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'titulo',
            'precio',
            'stock',
            'img',
            'descripcion'
        ]
        labels = {
            'id':'ID',
            'titulo':'TITULO',
            'precio':'PRECIO',
            'stock':'STOCK',
            'img':'IMAGEN',
            'descripcion': 'DESCRIPCION'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'titulo':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'precio':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows','type':'number'}),
            'img':forms.FileInput(attrs={'class':'form-control shadow-none'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control shadow-none'})
        }