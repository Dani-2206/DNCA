# Generated by Django 4.0.4 on 2022-06-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(verbose_name='numero de telefono'),
        ),
    ]