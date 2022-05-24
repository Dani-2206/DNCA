from django import forms
from django.forms import ModelForm,widgets
from .models import Colab

class SugerenciasForm(ModelForm):
    class Meta:
        model = Colab
        fields = ['nombre_u','nombre','apellido','email','telefono','contraseña']
        labels={
            'nombre_u':'Nombre Usuario',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'email':'Correo Electronico',
            'telefono':'Teléfono',
            'contraseña':'Contraseña'
        }

        widgets={
            'nombre_u': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre_u',
                    'id': 'nombre_u',
                    'placeholder': 'Nombre de usuario'
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
           'apellido': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'apellido',
                    'id': 'ap',
                    'placeholder': 'Nombre Completo'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Nombre@dominio.cl'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Número de contacto',
                }
            ),   
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'contraseña',
                    'name': 'contraseña',
                    'placeholder': 'Contraseña',
                }
            ),
        }

'''

class creaSugerenciasForm(ModelForm):
    class Meta:
        model = Colab
        fields = ['nombre','email','telefono','pais','direccion','contraseña', 'imagen']
        labels={
            'nombre':'Nombre Completo',
            'email':'Correo Electronico',
            'telefono':'Teléfono',
            'direccion':'Direccion',
            'pais':'Pais',
            'contraseña':'Contraseña',
            'imagen':'imagen'
        }

        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': 'Rut'
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
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Nombre@dominio.cl'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Número de contacto',
                }
            ),    
            'pais': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Pais',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'direccion',
                    'name': 'direccion',
                    'placeholder': 'Escriba aqui su Direccion',
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'contraseña',
                    'name': 'contraseña',
                    'placeholder': 'Contraseña',
                }
            ),
            'imagen': forms.FileInput(
            
                
            ),
        }
'''
