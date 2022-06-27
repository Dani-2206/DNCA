from django.db import models


class Empleados(models.Model):
    rut= models.CharField(max_length=50,verbose_name='Nombre de usuario',primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre del empleado')
    apellido=models.CharField(max_length=100, verbose_name='Nombre')
    email=models.CharField(max_length=100, verbose_name='apellido')
    telefono =models.IntegerField(verbose_name='numero de telefono')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')

    def __str__(self):
        return(self.nombre)
