from django.urls import path
from .views import crud, ingresar, modificar, eliminar

urlpatterns=[
    path('crud', crud, name="crude"),
    path('ingresar', ingresar, name="sugerenciase"),
    path('mod_e/<id>', modificar, name="modificarempleado"),
    path('elimi_e/<id>', eliminar, name="eliminarempleado"),
]
