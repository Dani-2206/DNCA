
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  crud,form_del_sugerencia,galeria,form_mod_sugerencia,sugerencias,tienda,agregarProducto,eliminarProducto,restarProducto,limpiarCarrito,catalogo




urlpatterns=[    
    path('galeria/', login_required(galeria), name="galeria"),
    path('sugerencias/',login_required(sugerencias), name="sugerencias"),
    path('crud/', login_required(crud), name="crud"),
    path('form_mod_sugerencia/<id>', login_required(form_mod_sugerencia), name="form_mod_sugerencia"),
    path('form_del_sugerencia/<id>', login_required(form_del_sugerencia), name="form_del_sugerencia") ,
    path('catalogo',login_required(catalogo),name="catalogo"),


    path('tienda/',login_required(tienda),name="carrito"),
    path('agregar/<int:producto_id>',login_required(agregarProducto),name="add"),
    path('eliminar/<int:producto_id>',login_required(eliminarProducto),name="del"),
    path('restar/<int:producto_id>',login_required(restarProducto),name="sub"),
    path('limpiar/',login_required(limpiarCarrito),name="CLS"),
    
]