# Generated by Django 3.2.3 on 2021-07-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_colab_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='colab',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuario'),
        ),
    ]
