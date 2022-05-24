from dataclasses import field, fields
from django.db import models

# Create your models here.

class Colab(models.Model):
    nombre_u = models.CharField(max_length=50,verbose_name='Nombre de usuario')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.CharField(max_length=100, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=9, verbose_name='Número de contacto')
    contraseña = models.CharField(max_length=35, verbose_name='Contraseña')

    def __str__(self):
        return(self.nombre_u)
        





