from django.urls import path
from .views import ListadoUsuario,crearusuario ,inicioU
from django.contrib.auth.decorators import login_required


urlpatterns=[    
    path('ver_u/',login_required(ListadoUsuario.as_view()),name='listar_usuario'),
    path('crear_u/',login_required(crearusuario.as_view()),name='registrar_usuario'),
    path('inicio_u',login_required(inicioU.as_view()),name='inicio')]