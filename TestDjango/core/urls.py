from codecs import namereplace_errors
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  crud,form_del_sugerencia,galeria,paginaprincipal,form_mod_sugerencia,sugerencias




urlpatterns=[    
    path('paginaP/', login_required(paginaprincipal), name="index"),
    path('galeria/', login_required(galeria), name="galeria"),
    path('sugerencias/',login_required(sugerencias), name="sugerencias"),
    path('crud/', login_required(crud), name="crud"),
    path('form_mod_sugerencia/<id>', login_required(form_mod_sugerencia), name="form_mod_sugerencia"),
    path('form_del_sugerencia/<id>', login_required(form_del_sugerencia), name="form_del_sugerencia") ,
]