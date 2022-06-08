from dataclasses import field
from tkinter import Widget
from tkinter.tix import Form
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Usuario

class formulariologin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(formulariologin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre usuario'

        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

        

class Formulario(forms.ModelForm):

    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
    attrs={
        'class':'form-control',
        'placeholder':'Ingrese su contraseña ',
        'id':'password1',
        'required':'required',
   }))

    password2=forms.CharField(label='Contraseña de Confirmación',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }))



    class Meta:
        model = Usuario
        fields = (  'username',
                    'nombres',
                    'telefono',
                    'apellidos',
                    'email'
        )
        
        Widgets ={
            'username' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre usuario',
                    'id':'Nombre_u',
                    'required':'required',
                }
            ),
            'nombres':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'Nombre',
                    'required':'required',
                }
            ),
            'telefono':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'Telefono',
                    'required':'required',

                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido',
                    'id':'apellido',
                    'required':'required',
                }
            ),
            
            'email':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'Nombre',
                    'required':'required',
                }
            ),


        }

def clean_password2(self):
    password1=self.cleaned_data.get('password1')
    password2=self.cleaned_data.get('password2')

    if password1 and password2 and password1 != password2 :
        raise forms.ValidationError('las contraseñas no conciden')
    return password2

def save(self,commit=True):
    user= super.save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
        user.save()
    return user
