from django.db import models

# Create your models here.
class Colab(models.Model):
    productoid = models.IntegerField(primary_key=True,verbose_name='ID del producto')
    nombre=models.CharField(max_length=50, verbose_name='nombre producto')
    imagen=models.ImageField(upload_to='usuario',blank=True , null=True)
    descripcion=models.CharField(max_length=50, verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='Valor del profucto',blank=True , null=True)

    def __str__(self):
        return(self.pais)







