from django import forms
from django.forms import ModelForm,widgets
from .models import Colab


class SugerenciasForm(ModelForm):
    class Meta:
        model = Colab
        fields = ['productoid','nombre','imagen','descripcion','precio']
        labels={
            'productoid':'Ingrese el id del producto',
            'nombre':'Nombre del producto',
            'imagen':'imagen',
            'descripcion':'descripcion',
            'precio':'ingrese el precio del producto'
        }

        widgets={
            'productoid': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'id p',
                    'name': 'id p',
                    'placeholder': 'id p'
                }
            ),    
            'nombre': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre',
                    'id': 'nombre',
                    'placeholder': 'Nombre Completo'
                }
            ),
            'imagen': forms.FileInput(
            
                
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'controls',
                    'id': 'descripcion',
                    'name': 'descripcion',
                    'placeholder': 'descripcion'
                }
            ),  
            'precio': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'precio',
                    'name': 'precio',
                    'placeholder': '1000'
                }

            )
        }

