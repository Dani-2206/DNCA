from django.urls import path
from .views import crud, ingresar, form_mod_sugerencia, form_del_sugerencia

urlpatterns=[
    path('crud', crud, name="crude"),
    path('ingresar', ingresar, name="sugerenciase"),
    path('mod_e/<id>', form_mod_sugerencia, name="modificarempleado"),
    path('elimi_e/<id>', form_del_sugerencia, name="eliminarempleado"),
]
