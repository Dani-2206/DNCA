from django import forms
from .models import Empleados


class form_Empleados(forms.ModelForm):
    class Meta:
        model = Empleados
        fields =['rut','nombre','apellido','email','telefono','cargo']
        labels={
            'rut': 'ingrese el rut del empleado',
            'nombre':'ingrese el nombre del empleado',
            'apellido':'ingrese el apellido del empleado',
            'email':'ingrese el email del empleado',
            'telefono':'ingrese el telefono del empleado',
            'cargo':'ingrese el cargo del empleado'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': '123342-1'
                }
            ),    
            'nombre': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre',
                    'id': 'nombre',
                    'placeholder': 'Jose'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'apellido',
                    'id': 'apellido',
                    'placeholder': 'Manielito '
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'email',
                    'id': 'email',
                    'placeholder': 'Manielito@gmail.com '
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': '123131'
                }

            ),
            'cargo': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'cargo',
                    'id': 'cargo',
                    'placeholder': 'Jefe de bodega'
                }
            ),



        }