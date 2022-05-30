from django import forms
from django.forms import ModelForm,widgets
from .models import Colab


class SugerenciasForm(ModelForm):
    class Meta:
        model = Colab
        fields = ['productoid','nombre','imagen','descripcion']
        labels={
            'productoid':'Ingrese el id',
            'nombre':'Nombre Completo',
            'imagen':'imagen',
            'descripcion':'descripcion'
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
        }

