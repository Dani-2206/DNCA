from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self,email,nombres,apellidos,telefono,username,password= None):
        if not email:
            raise ValueError("se debe ingresar un email")
        if not username:
            raise ValueError("se debe ingresar un usuario")
        
        
        usuario = self.model(
            username=username, 
            email = self.normalize_email(email),
            nombres=nombres,
            telefono=telefono,
            apellidos=apellidos
        )

        usuario.set_password(password); 
        usuario.save(using=self._db)
        return usuario



    def create_superuser(self,username,apellidos,telefono,nombres,email,password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password,
            telefono=telefono,
            apellidos=apellidos
        )

        usuario.usuario_administrador= True
        usuario.save(using=self._db)
        return usuario





class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=50,verbose_name='Nombre de usuario',primary_key=True)
    email = models.CharField(max_length=100, verbose_name='Correo Electronico')
    nombres=models.CharField(max_length=100, verbose_name='Nombre')
    apellidos=models.CharField(max_length=100, verbose_name='apellido')
    telefono =models.IntegerField(verbose_name='numero de telefono')

    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','nombres','telefono','apellidos']
                               

    def __str__(self):
        return self.username 

    def has_perm(self,perm,obj = None):
        return True

           
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

