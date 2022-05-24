from django.db import models

# Create your models here.

class Colab(models.Model):
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='rut')
 
    nombre = models.CharField(max_length=50,verbose_name='Nombre de usuario')
    email = models.CharField(max_length=100, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=9, verbose_name='Número de contacto')
    pais = models.CharField(max_length=20, verbose_name='Pais')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    contraseña = models.CharField(max_length=35, verbose_name='Contraseña')
    imagen = models.ImageField(upload_to='usuario',blank=True , null=True)

    def __str__(self):
        return(self.rut)





