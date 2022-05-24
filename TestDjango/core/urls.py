from django.urls import path
from .views import paginaprincipal, galeria, sugerencias, crud, form_mod_sugerencia, form_del_sugerencia

urlpatterns=[
    path('', paginaprincipal, name="paginaprincipal"),
    path('galeria/', galeria, name="galeria"),
    path('sugerencias/', sugerencias, name="sugerencias"),
    path('crud/', crud, name="crud"),
    path('form_mod_sugerencia/<id>', form_mod_sugerencia, name="form_mod_sugerencia"),
    path('form_del_sugerencia/<id>', form_del_sugerencia, name="form_del_sugerencia") 
]